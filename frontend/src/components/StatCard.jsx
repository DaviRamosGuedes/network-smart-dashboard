export default function StatCard({ title, value, color }) {
    const colors = {
        blue: "from-blue-600 to-blue-400",
        green: "from-green-600 to-green-400",
        red: "from-red-600 to-red-400",
    }

    return (
        <div className={`bg-gradient-to-r ${colors[color]} p-6 rounded-2xl`}>
            <p className="text-sm opacity-80">{title}</p>
            <h2 className="text-3xl font-bold">{value}</h2>
        </div>
    )
}