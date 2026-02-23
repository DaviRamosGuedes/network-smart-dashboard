export default function Sidebar() {
    return (
        <div className="w-64 bg-slate-900 p-6">
            <h2 className="text-xl font-bold mb-8">NetScan</h2>

            <nav className="space-y-4 text-slate-400">
                <p className="text-white">Dashboard</p>
                <p>Devices</p>
                <p>Settings</p>
            </nav>
        </div>
    )
}