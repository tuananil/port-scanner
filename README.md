# Simple TCP Port Scanner

A lightweight and efficient Command-Line Interface (CLI) based TCP Port Scanner written in Python. This project is designed to perform basic network reconnaissance by scanning specified host ports to determine their operational status.

## Features
* **TCP Connection Scanning:** Utilizes Python's native `socket` library to establish standard TCP connections.
* **Host Resolution:** Automatically resolves domain names (e.g., `localhost`) to their respective IPv4 addresses.
* **Targeted Scanning:** Iterates through standard ports (1-100) with a built-in timeout mechanism to optimize performance and prevent hanging connections.
* **Clean CLI Output:** Provides real-time feedback, explicitly logging discovered open ports.

## Architecture & Concepts Covered
* **Network Sockets:** Implements standard internet communication endpoints via `socket.socket`.
* **Exception Handling:** Utilizes `try-except` blocks to handle connection timeouts and unreachable hosts gracefully without crashing the script.
* **Address Translation:** Employs `socket.gethostbyname` for DNS resolution.

## Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your system.

### Installation & Execution
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/tuananil/port-scanner.git](https://github.com/tuananil/port-scanner.git)
   cd port-scanner
