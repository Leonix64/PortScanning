import os
import csv
import socket
import json
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from fpdf import FPDF

# Función para generar un informe CSV basado en los resultados del escaneo
def generate_csv_report(ports_occupied_tcp, ports_free_tcp, ports_occupied_udp, ports_free_udp, report_folder, target_ip):
    csv_path = os.path.join(report_folder, 'ports_report.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'Port', 'Protocol', 'Status', 'Service']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Escribir información de puertos TCP ocupados en el informe CSV
        for port in ports_occupied_tcp:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'TCP', 'Status': 'Busy', 'Service': service})

        # Escribir información de puertos TCP libres en el informe CSV
        for port in ports_free_tcp:
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'TCP', 'Status': 'Free', 'Service': ''})

        # Escribir información de puertos UDP ocupados en el informe CSV
        for port in ports_occupied_udp:
            try:
                service = socket.getservbyport(port, 'udp')
            except OSError:
                service = 'Unknown'
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'UDP', 'Status': 'Busy', 'Service': service})

        # Escribir información de puertos UDP libres en el informe CSV
        for port in ports_free_udp:
            writer.writerow({'IP': target_ip, 'Port': port, 'Protocol': 'UDP', 'Status': 'Free', 'Service': ''})

    print("CSV report generated successfully.")

    # Exportar a formato JSON
    json_data = {
        'IP': target_ip,
        'Ports': {
            'TCP': {
                'Occupied': ports_occupied_tcp,
                'Free': ports_free_tcp
            },
            'UDP': {
                'Occupied': ports_occupied_udp,
                'Free': ports_free_udp
            }
        }
    }
    json_path = os.path.join(report_folder, 'ports_report.json')
    with open(json_path, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    print("JSON report generated successfully.")

    # Exportar a formato XML
    xml_root = Element('PortsReport')
    ip_element = SubElement(xml_root, 'IP')
    ip_element.text = target_ip
    tcp_element = SubElement(xml_root, 'TCP')
    udp_element = SubElement(xml_root, 'UDP')

    for port in ports_occupied_tcp:
        occupied_element = SubElement(tcp_element, 'Occupied')
        occupied_element.text = str(port)
    for port in ports_free_tcp:
        free_element = SubElement(tcp_element, 'Free')
        free_element.text = str(port)
    for port in ports_occupied_udp:
        occupied_element = SubElement(udp_element, 'Occupied')
        occupied_element.text = str(port)
    for port in ports_free_udp:
        free_element = SubElement(udp_element, 'Free')
        free_element.text = str(port)

    xml_string = tostring(xml_root, 'utf-8')
    xml_formatted = parseString(xml_string)
    xml_path = os.path.join(report_folder, 'ports_report.xml')
    with open(xml_path, 'w') as xmlfile:
        xmlfile.write(xml_formatted.toprettyxml())
    print("XML report generated successfully.")

    # Exportar a formato PDF (requiere la biblioteca fpdf)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Port Report for IP: {target_ip}", ln=True)
    pdf.cell(200, 10, '', ln=True)  # Agregar espacio

    pdf.cell(200, 10, "TCP Ports:", ln=True)
    pdf.cell(200, 10, f"Occupied: {', '.join(map(str, ports_occupied_tcp))}", ln=True)
    pdf.cell(200, 10, f"Free: {', '.join(map(str, ports_free_tcp))}", ln=True)
    pdf.cell(200, 10, '', ln=True)  # Agregar espacio

    pdf.cell(200, 10, "UDP Ports:", ln=True)
    pdf.cell(200, 10, f"Occupied: {', '.join(map(str, ports_occupied_udp))}", ln=True)
    pdf.cell(200, 10, f"Free: {', '.join(map(str, ports_free_udp))}", ln=True)

    pdf_path = os.path.join(report_folder, 'ports_report.pdf')
    pdf.output(pdf_path)
    print("PDF report generated successfully.")