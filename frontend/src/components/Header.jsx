export default function Header({ onScan }) {
    return (
        <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold">Network Dashboard</h1>

            <button
                onClick={onScan}
                className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-xl"
            >
                Scan Network
            </button>
        </div>
    )
}