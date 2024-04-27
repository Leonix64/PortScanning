# Escáner de Puertos y Generador de Informes

Este proyecto consiste en un escáner de puertos TCP y UDP en una dirección IP especificada, junto con la generación de un informe CSV que detalla los puertos ocupados y libres, así como la información del servicio asociado a cada puerto.

## Funcionalidades

- **Escaneo de Puertos TCP y UDP:** Utiliza sockets para escanear puertos en un rango especificado y determinar cuáles están ocupados y cuáles están libres.
  
- **Generación de Informe:** Crea un informe CSV detallado que incluye la dirección IP, el puerto, el protocolo, el estado (ocupado o libre) y el servicio asociado (si está disponible) para cada puerto escaneado.

## Requisitos

- Python 3.x instalado en tu sistema.
  
- Bibliotecas estándar de Python: `socket`, `concurrent.futures`, `os`, `csv`.

## Uso

1. Clona este repositorio en tu máquina local.
   
2. Asegúrate de tener los requisitos mencionados instalados.

3. Configura las variables necesarias en el archivo `config.py`, como la dirección IP de destino y el rango de puertos a escanear.

4. Ejecuta el script `main.py` para iniciar el escaneo de puertos y generar el informe CSV en la carpeta especificada.

## Estructura de Archivos

- `main.py`: Punto de entrada del programa que inicia el escaneo de puertos y la generación del informe.
  
- `scanner.py`: Contiene las funciones para escanear puertos TCP y UDP de manera concurrente.
  
- `report_generator.py`: Define la función para generar el informe CSV basado en los resultados del escaneo.
  
- `config.py`: Archivo de configuración que contiene las variables como la dirección IP, el rango de puertos y la carpeta para el informe.

## Contribución

Si deseas contribuir a este proyecto, puedes enviar sugerencias, informar errores o enviar solicitudes de extracción (pull requests) para mejorar la funcionalidad o el código.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
