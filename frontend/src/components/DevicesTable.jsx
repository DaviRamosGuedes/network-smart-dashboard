export default function DevicesTable({ devices }) {
    return (
        <div className="bg-slate-900 rounded-2xl p-6">
            <h3 className="text-xl mb-4">Devices</h3>

            <table className="w-full text-left">
                <thead className="text-slate-400">
                    <tr>
                        <th>IP</th>
                        <th>MAC</th>
                        <th>Hostname</th>
                        <th>Status</th>
                    </tr>
                </thead>

                <tbody>
                    {devices.map((d) => (
                        <tr key={d.id} className="border-t border-slate-800">
                            <td className="py-3">{d.ip}</td>
                            <td>{d.mac}</td>
                            <td>{d.hostname || "-"}</td>
                            <td>
                                <span
                                    className={`px-3 py-1 rounded-full text-sm ${d.status === "up"
                                        ? "bg-green-500/20 text-green-400"
                                        : "bg-red-500/20 text-red-400"
                                        }`}
                                >
                                    {d.status}
                                </span>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}