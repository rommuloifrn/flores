import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"oi man!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # UDP
MESSAGE = str.encode(input("Qual a quantidade de pétalas? "))
#sock.bind((UDP_IP, UDP_PORT))
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print("received message: %s" % data)
    
while True:
    MESSAGE = str.encode(input("Retire a pétala!"))
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    
    data = data.decode('utf-8')

    if (data == "Ele(a) te ama!") or (data == "Ele(a) não te ama!"):
        break
    