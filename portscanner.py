import socket
import errno
import json
import requests
import sys
import shodan


# print(sys.version_info)
# print(sys.version)

SHODAN_API_KEY = "12odDOcZyLDJ2HZuNMrvUqCbhsJKqlpC" 
api = shodan.Shodan(SHODAN_API_KEY)

# A dictionary of common port numbers and their commonly associated protocols


common_protocols = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    993: "IMAP",
    995: "POP3",
}


# When I tried socket.connect_ex like shown in the Python documentation, I was getting an AttributeError: module 'socket' has no attribute 'connect_ex'
# After spending time doing some research I found a workaround others had. Function connect_ex is not my code, but I am sure glad I found it.

# def connect_ex(target_ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         sock.connect((target_ip, port))
#         return True  # Connection succeeded
#     except socket.error as e:
#         if e.errno == errno.ECONNREFUSED:
#             return False  # Connection refused
#         else:
#             raise  # Some other error
#     finally:
#         sock.close()


def scan_ports(target_ip, port, ports_open, ports_closed, ports_error): 
    """Attempts to make a connection to the target IP and port number and sets a time of two seconds. If the connection is successful, the port is open. If the connection is unsuccessful, the port is closed."""
    
    
    try:
        '''This attempts to create a TCP connection using an IPV4 address. AF_INET tells the script that it is using an IPV4 while AF_INET6 would be for a IPV6. SOCK_STREAM is to create the TCP socket connection. TCP is used because it is more reliable than UDP which would use SOCK_DGRAM. Since we are attempting to create and confirm a connection, we would need to use TCP because UDP is considered unreliable and connectionless. '''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            banner = sock.recv(1024).decode()
            ports_open.add(port)
            return "Open", banner
        else:
            ports_closed.add(port)
            return "Closed", ""
    except socket.timeout:
        return "Timeout", "Connection timed out"    
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            ports_closed.add(port)
            return "Close", ""  # Connection refused 
        elif e.errno == errno.ETIMEDOUT:
            return "Error", "Connection timed out" 
        elif e.errno == errno.EHOSTUNREACH:
            return "Error", "Host is unreachable"
        elif e.errno == errno.EHOSTNOTFOUND:
            return "Error", "Host not found"
        elif e.errno == errno.EADDRNOTAVAIL:
            return "Error", "Address not available"
        elif e.errno == errno.EADDRINUSE:
            return "Error", "Address in use"
        elif e.errno == errno.EALREADY:
            return "Error", "Address already in use"
        elif e.errno == errno.EWOULDBLOCK:
            return "Error", "Operation would block"
        elif e.errno == errno.EACCES:
            return "Error", "Permission denied"
        

        else:
            ports_error.add(port)
            return "Error", f"Other error: {e}" 






def main():
    """Starts a loop to iterate through a range of ports. For each port, the scan_ports function is called and the results are printed. For speed and effiency, only the most common 1024 ports are scanned. Attempting to scan all 65535 ports will take a long time."""

    # For initial testing, loopback ip will be used.
    # Future version will include argparse to enter the ip address or URL
    # Starts with port 1 as port 0 is a reserved port
    target_ip = "127.0.0.1"
    starting_port = 999
    ending_port = 1026

    #Creating three sets for the port status 
    # ports_open
    # ports_closed
    # ports_error
    ports_open = set()
    ports_closed = set()
    ports_error = set() 





    # Reminder to self, when looping through a range of defined range of numbers make sure to use + 1 to include the last number in the range. The for loop calls the scan_ports function.

    for port_numbers in range(starting_port, ending_port + 1):
        status, banner = scan_ports(target_ip, port_numbers, ports_open, ports_closed, ports_error)
        protocol_name = common_protocols.get(port_numbers, "Unknown")

        print(f"Port {port_numbers} is {status}. Protocol is ({protocol_name})")
        # If the port is open it will attempt to grab the banner
        if status == "Open":
            '''Creates a connecion to the Shodan API to get more information about the port or service.'''
            try:
                results = api.search(f'port:{port_numbers}')
                print("*** Shodan Results ***")
                for result in results['matches']:
                    print(f"IP: {result['ip_str']}")
                    print(f"Banner: {result['data']}")
                    print(f"Hostnames: {result.get('hostnames', 'Not Available')}")
                    # print(result)
            
            except shodan.APIError as e:
                print(f"Shodan Error for Port {port_numbers}: {e}")



            print(f"Banner: {banner}")
        # If the port is closed it will print a messge
        else:
            print("No banner received")
    results_dict = {
        "open_ports": list(ports_open),
        "closed_ports": list(ports_closed),
        "error_ports": list(ports_error)
    }

    # Writing the results to a json file
    with open("ports.json", "w") as f:  
        json.dump(results_dict, f)


if __name__ == "__main__":
    main()
