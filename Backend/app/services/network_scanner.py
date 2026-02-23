import nmap
import socket


def get_local_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip.rsplit('.', 1)[0] + '.0/24'


def scan_network(rede=None):

    if rede is None:
        rede = get_local_network()

    scanner = nmap.PortScanner()
    scanner.scan(hosts=rede, arguments="-sn -PR")

    devices = []

    for host in scanner.all_hosts():
        mac = scanner[host]['addresses'].get('mac', 'N/A')

        devices.append({
            "ip": host,
            "mac": mac,
            "hostname": scanner[host].hostname(),
            "status": scanner[host].state()
        })

    return devices