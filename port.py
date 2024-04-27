import socket
import concurrent.futures
import csv

def scan_ports():
    ports_occupied_tcp = []
    ports_free_tcp = []
    ports_occupied_udp = []
    ports_free_udp = []

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                result = sock.connect_ex(('192.168.1.1', port))
                if result == 0:
                    ports_occupied_tcp.append(port)
                    status = "Busy"
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except OSError:
                        service = "Unknown"
                else:
                    ports_free_tcp.append(port)
                    status = "Free"
                    service = ""
                print(f"TCP Port {port}: {status} ({service})")
        except Exception as e:
            print(f"TCP Scan error in port {port}: {e}")

    def scan_udp_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(2)
                sock.sendto(b'', ('192.168.1.67', port))
                data, _ = sock.recvfrom(1024)
                ports_occupied_udp.append(port)
                status = "Busy"
                try:
                    service = socket.getservbyport(port, 'udp')
                except OSError:
                    service = "Unknown"
                print(f"UDP Port {port}: {status} ({service})")
        except Exception as e:
            ports_free_udp.append(port)
            print(f"UDP Scan error in port {port}: {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results_tcp = [executor.submit(scan_port, port) for port in range(1, 1025)]
        results_udp = [executor.submit(scan_udp_port, port) for port in range(1, 1025)]

    return ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp

def generate_csv_report(ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp):
    with open('ports_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Port', 'Protocol', 'Status', 'Service']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for port in ports_occupied_tcp:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'Port': port, 'Protocol': 'TCP', 'Status': 'Busy', 'Service': service})

        for port in ports_free_tcp:
            writer.writerow({'Port': port, 'Protocol': 'TCP', 'Status': 'Free', 'Service': ''})

        for port in ports_occupied_udp:
            try:
                service = socket.getservbyport(port, 'udp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'Port': port, 'Protocol': 'UDP', 'Status': 'Busy', 'Service': service})

        for port in ports_free_udp:
            writer.writerow({'Port': port, 'Protocol': 'UDP', 'Status': 'Free', 'Service': ''})

    print("CSV report generated successfully.")

ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp = scan_ports()
generate_csv_report(ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp)