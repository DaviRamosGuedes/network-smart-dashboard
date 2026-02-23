import { useEffect, useState } from "react"
import Sidebar from "../components/Sidebar"
import Header from "../components/Header"
import DevicesTable from "../components/DevicesTable"
import StatCard from "../components/StatCard"

export default function Dashboard() {
  const [devices, setDevices] = useState([])

  async function loadDevices() {
    const res = await fetch("http://127.0.0.1:8000/devices")
    const data = await res.json()
    setDevices(data)
  }

  async function scanNetwork() {
    await fetch("http://127.0.0.1:8000/scan", {
      method: "POST",
    })

    loadDevices()
  }

  useEffect(() => {
    loadDevices()
    const interval = setInterval(loadDevices, 5000)
    return () => clearInterval(interval)
  }, [])

  const online = devices.filter(d => d.status === "up").length
  const offline = devices.length - online

  return (
    <div className="flex bg-slate-950 text-white min-h-screen">
      <Sidebar />

      <div className="flex-1 p-6 space-y-6">
        <Header onScan={scanNetwork} />

        <div className="grid grid-cols-3 gap-6">
          <StatCard title="Total Devices" value={devices.length} color="blue" />
          <StatCard title="Online" value={online} color="green" />
          <StatCard title="Offline" value={offline} color="red" />
        </div>

        <DevicesTable devices={devices} />
      </div>
    </div>
  )
}