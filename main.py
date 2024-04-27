import os
from scanner import scan_ports
from report_generator import generate_csv_report
from config import REPORT_FOLDER, TARGET_IP

if __name__ == "__main__":
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

    ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp = scan_ports()
    generate_csv_report(ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp, REPORT_FOLDER, TARGET_IP)

    print("CSV report generated successfully.")