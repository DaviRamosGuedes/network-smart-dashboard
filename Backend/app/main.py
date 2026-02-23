from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import asyncio

from app.database import engine, SessionLocal, Base
from app.models.device import Device
from app.services.network_scanner import scan_network
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

# 🔌 conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🧠 FUNÇÃO DE SCAN (reutilizável)
def run_network_scan():
    db = SessionLocal()

    print("🔎 Iniciando scan da rede...")

    devices = scan_network()

    # ⚠️ marca todos como offline antes do scan
    db.query(Device).update({Device.status: "down"})

    for device in devices:
        device_data = device.copy()

        mac = device_data.get("mac") or device_data.get("ip")
        device_data["mac"] = mac

        existing = db.query(Device).filter(Device.mac == mac).first()

        if existing:
            existing.ip = device_data.get("ip")
            existing.hostname = device_data.get("hostname")
            existing.status = device_data.get("status")
            existing.last_seen = datetime.now(timezone.utc)

        else:
            device_data["last_seen"] = datetime.now(timezone.utc)
            db.add(Device(**device_data))

    db.commit()
    db.close()

    print("✅ Scan finalizado")


# 🚀 SCAN AUTOMÁTICO AO INICIAR
@asynccontextmanager
async def lifespan(app: FastAPI):

    async def start_scan():
        await asyncio.to_thread(run_network_scan)

    asyncio.create_task(start_scan())

    yield

app = FastAPI(lifespan=lifespan)

### liberacao cors para o frontend ter acesso
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📡 LISTAR TODOS
@app.get("/devices")
def list_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()


# 🟢 ONLINE
@app.get("/devices/online")
def online_devices(db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.status == "up").all()


# 🕒 RECENTES (últimos 5 min)
@app.get("/devices/recent")
def recent_devices(db: Session = Depends(get_db)):
    from datetime import timedelta

    limite = datetime.now(timezone.utc) - timedelta(minutes=5)

    return db.query(Device).filter(Device.last_seen >= limite).all()


# 🔎 SCAN MANUAL
@app.post("/scan")
def scan():
    run_network_scan()
    return {"message": "Scan finalizado"}