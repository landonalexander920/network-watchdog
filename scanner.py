import socket  # Python's built-in networking library

# Ask for a target and define the ports to check
target = input("Enter IP to scan: ")
ports = [22, 80, 443, 8000]  # SSH, HTTP, HTTPS, common dev server port

# Try to connect to each port and report whether it's open
for port in ports:
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP socket
    scanner_socket.settimeout(0.5)  # Wait at most half a second per port
    result = scanner_socket.connect_ex((target, port))  # Returns 0 if the connection succeeds
    if result == 0:
        print(f"[OPEN]   Port {port}")
    else:
        print(f"[closed] Port {port}")
    scanner_socket.close()  # Close the connection before the next port

# Stage 2: discover every device on the local subnet
