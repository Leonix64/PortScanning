import os
import csv
import socket

# Función para generar un informe CSV basado en los resultados del escaneo
def generate_csv_report(ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp, report_folder, target_ip):
    csv_path = os.path.join(report_folder, 'ports_report.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'Port', 'Protocol', 'Status', 'Service']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Escribir información de puertos TCP ocupados en el informe
        for port in ports_occupied_tcp:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'TCP', 'Status': 'Busy', 'Service': service})

        # Escribir información de puertos TCP libres en el informe
        for port in ports_free_tcp:
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'TCP', 'Status': 'Free', 'Service': ''})

        # Escribir información de puertos UDP ocupados en el informe
        for port in ports_occupied_udp:
            try:
                service = socket.getservbyport(port, 'udp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'UDP', 'Status': 'Busy', 'Service': service})

        # Escribir información de puertos UDP libres en el informe
        for port in ports_free_udp:
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'UDP', 'Status': 'Free', 'Service': ''})

    print("CSV report generated successfully.") 
