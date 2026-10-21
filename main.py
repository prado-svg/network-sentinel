print("Welcome to Network Sentinel!")
print("Which IP adress do you want to verify?")
IP = input()
if IP == "127.0.0.1":
    print("Loopback address detected!")
else:
    print("Other IP address.")
