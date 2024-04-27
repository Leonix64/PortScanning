import socket
import concurrent.futures
from config import TARGET_IP, PORT_RANGE_START, PORT_RANGE_END

def scan_ports():
    ports_occupied_tcp = []
    ports_free_tcp = []
    ports_occupied_udp = []
    ports_free_udp = []

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                result = sock.connect_ex((TARGET_IP, port))
                if result == 0:
                    ports_occupied_tcp.append(port)
                else:
                    ports_free_tcp.append(port)
        except Exception as e:
            print(f"TCP Scan error in port {port}: {e}")

    def scan_udp_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(2)
                sock.sendto(b'', (TARGET_IP, port))
                data, _ = sock.recvfrom(1024)
                ports_occupied_udp.append(port)
        except Exception as e:
            ports_free_udp.append(port)
            print(f"UDP Scan error in port {port}: {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results_tcp = [executor.submit(scan_port, port) for port in range(PORT_RANGE_START, PORT_RANGE_END + 1)]
        results_udp = [executor.submit(scan_udp_port, port) for port in range(PORT_RANGE_START, PORT_RANGE_END + 1)]

    return ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp