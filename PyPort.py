import socket

# Check that the (address, port) is reachable or not using TCP
def check_port_reachable(address, port, timeout: float=3) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #AF_INET = IPv4 / AF_INET6 = IPv6
    sock.settimeout(timeout)

    try:
        sock.connect((address, port))       # Try connection
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return True
    except (socket.timeout, socket.error):  # Connection failed
        sock.close()
        return False

# Loop to handle script crash when not inputing number
while True:
    try:
        address = (input("Enter an IP address or hostname: "))
        port = int(input("Enter a port: "))
    except ValueError:
        print("Invalid input!")
        continue        # Restart loop after error

    result = check_port_reachable(address, port)

    # Display result
    if result:
        print(f"Port {port} on {address} is OPEN!")
    else:
        print(f"Port {port} on {address} is CLOSED or unreachable")

    # Ask if to scan again
    scan_again = input(("Wish to scan again? y/n "))
    if scan_again == "y":
        continue
    elif scan_again == "n":
        break
    else:
        print("Not valid input")
        break
