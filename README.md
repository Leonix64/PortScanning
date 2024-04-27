# Port Scanner and Report Generator

This project is a port scanner for TCP and UDP ports on a specified IP address, along with a CSV report generator detailing occupied and free ports, along with associated service information for each scanned port.

## Features

- **TCP and UDP Port Scanning:** Utilizes sockets to scan ports in a specified range and determine which are occupied and which are free.
  
- **Report Generation:** Generates a detailed CSV report including IP address, port number, protocol, status (occupied or free), and associated service (if available) for each scanned port.

## Requirements

- Python 3.x installed on your system.
  
- Python standard libraries: `socket`, `concurrent.futures`, `os`, `csv`.

## Usage

1. Clone this repository to your local machine.
   
2. Make sure you have the mentioned requirements installed.

3. Configure necessary variables in the `config.py` file, such as the target IP address and port range to scan.

4. Run the `main.py` script to start port scanning and generate the CSV report in the specified folder.

## File Structure

- `main.py`: Entry point of the program that initiates port scanning and report generation.
  
- `scanner.py`: Contains functions for concurrent TCP and UDP port scanning.
  
- `report_generator.py`: Defines the function to generate the CSV report based on scan results.
  
- `config.py`: Configuration file containing variables like target IP, port range, and report folder.

## Contribution

If you wish to contribute to this project, you can send suggestions, report bugs, or submit pull requests to improve functionality or code.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.
