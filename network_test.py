# import socket


# def scan_ports(target_ip, port):
#     """Attempts to make a connection to the target IP and port number and sets a time of two seconds. If the connection is successful, the port is open. If the connection is unsuccessful, the port is closed."""

#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(2)
#         result = sock.connect_ex((target_ip, port))

#         if result == 0:
#             return "Open"
#         else:
#             return "Closed"
#     except socket.error:
#         return "Error"


# if __name__ == "__main__":
#     target_ip = "127.0.0.1"
#     port = 443

#     status = scan_ports(target_ip, port)
#     print(f"Port {port} is {status}")


# import socket


# def scan_ports(target_ip, port):
#     """Attempts to make a connection to the target IP and port number and sets a time of two seconds. If the connection is successful, the port is open. If the connection is unsuccessful, the port is closed."""

#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(2)
#         result = sock.connect_ex((target_ip, port))

#         if result == 0:
#             banner = sock.recv(1024).decode()
#             return "Open", banner
#         else:
#             return "Closed", ""
#     except socket.error:
#         return "Error", ""


# if __name__ == "__main__":
#     target_ip = "127.0.0.1"
#     port = 22

#     status, banner = scan_ports(target_ip, port)
#     print(f"Port {port} is {status}")
#     if status == "Open":
#         print(f"Banner: {banner}")


# import socket


# def scan_ports(target_ip, port):
#     """Attempts to make a connection to the target IP and port number and sets a time of two seconds. If the connection is successful, the port is open. If the connection is unsuccessful, the port is closed."""

#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(2)
#         result = sock.connect_ex((target_ip, port))

#         if result == 0:
#             banner = sock.recv(1024).decode()
#             return "Open", banner
#         else:
#             return "Closed", ""
#     except socket.error as e:
#         return "Error", f"Error: {e}"


# if __name__ == "__main__":
#     target_ip = "127.0.0.1"
#     port = 8080

#     status, banner = scan_ports(target_ip, port)
#     print(f"Port {port} is {status}")
#     if status == "Open":
#         print(f"Banner: {banner}")
import socket


# def scan_ports(target_ip, port):
#     """Attempts to make a connection to the target IP and port number and sets a time of two seconds. If the connection is successful, the port is open. If the connection is unsuccessful, the port is closed."""

#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(2)
#         result = sock.connect_ex((target_ip, port))

#         if result == 0:
#             banner = sock.recv(1024).decode()
#             return "Open", banner
#         else:
#             return "Closed", ""
#     except socket.error as e:
#         return "Error", f"Error: {e}"


# if __name__ == "__main__":
#     target_ip = "8.8.8.8"
#     port = 53

#     status, banner = scan_ports(target_ip, port)
#     print(f"Port {port} is {status}")
#     if status == "Open":
#         print(f"Banner: {banner}")



with open("ports.txt", "w") as f:
    ports = f.write().splitlines()