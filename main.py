def validate_ip(IP):
    parts = IP.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
            if not part.isdigit():
                return False

            number = int(part)

            if number > 255:
                return False

            if len(part) > 1 and part[0] == "0":
                return False

    return True

#mai

print("Welcome to Network Sentinel!")

IP = input("Enter an IP address: ")

if validate_ip(IP):
    print("Valid IPv4 address!")

    if IP == "127.0.0.1":
        print("Loopback address detected!")
    else:
    	print("Other IP address.")

else:
    print("Invalid IPv4 address!")

