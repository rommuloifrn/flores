import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005




print(f"debug: ip {UDP_IP} na porta {UDP_PORT}")

# cria socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia mensagem para o servidor
print("Qual a quantidade de pétalas?\n")
petalas_qtd = str.encode(input())
sock.sendto(petalas_qtd, (UDP_IP, UDP_PORT)) 

data, addr = sock.recvfrom(1024) # recebe mensagem do servidor, buffer de 1024 bytes
print("mensagem recebida: %s" % data.decode('utf-8'))
    
# itera a quantidade de pétalas
for x in range(int(petalas_qtd.decode('utf-8'))):
    
    # envia a retirada da pétala para o server
    print("Retire a pétala!\n")
    mensagem = str.encode(input())
    sock.sendto(mensagem, (UDP_IP, UDP_PORT))

    # recebe resposta do servidor
    data, addr = sock.recvfrom(1024)
    print("mensagem recebida: %s" % data.decode('utf-8'))
    
    data = data.decode('utf-8')
    
# recebe resultado
data, addr = sock.recvfrom(1024)
print("mensagem recebida: %s" % data.decode('utf-8'))