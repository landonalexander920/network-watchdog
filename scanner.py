import socket  #grabs pythons networking toolbox

#check doors/ports wtv u wana call it lol
target = input("Enter IP to scan: ")
ports = [22, 80, 443, 8000]

# created a loop to run , to KNOCK on every door boiii
for port in ports:
    scanner_app_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # scanner app door open
    scanner_app_socket.settimeout(0.5) #knock for .5 seconds
    result = scanner_app_socket.connect_ex((target, port))
    if result == 0:     #0 = the door opened, any other number it didnt open.         # == means "is this equal to"      #if target door answered/door is open
        print(f"[OPEN]  Port {port}")
    else:
        print(f"[closed] Port {port}")
    scanner_app_socket.close() # scanner app door closed

#Stage 2: Find every device on my network, really meaning subnet. x.x.x.x





