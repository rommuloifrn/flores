import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
mandou = False
bem_me_quer = False
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    petalas_qtd = int(data)
    print("Quantidade de Petalas: %s" % petalas_qtd)
    MESSAGE = b'servidor confirma!'
    if mandou == False:
        sock.sendto(MESSAGE, addr)
        mandou = True
    while petalas_qtd > 0:
        data, addr = sock.recvfrom(1024)
        petalas_qtd -= 1 
        mensagem = str(petalas_qtd)
        if petalas_qtd % 2 == 0:
            mensagem = "Bem me Quer"
            bem_me_quer = True
        if petalas_qtd % 2 == 1:
            mensagem = "Mal me Quer"
            bem_me_quer = False
        sock.sendto(str.encode(mensagem), addr)
    
    if bem_me_quer == True:
        mensagem = "Ele(a) te ama!"
    else:
        mensagem = "Ele(a) não te ama!"
    sock.sendto(str.encode(mensagem), addr)
    break