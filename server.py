import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT)) # liga socket a endereço

conexao_inicial = True
bem_me_quer = False

# laço de listening de mensagem
while True:
    # recebe a quantidade de pétalas
    data, addr = sock.recvfrom(1024)
    petalas_qtd = int(data)
    print("Quantidade de Petalas: %s" % petalas_qtd)
    
    # checagem de conexão
    mensagem = b'servidor confirma!'
    if conexao_inicial == True:
        sock.sendto(mensagem, addr)
        conexao_inicial = False
    
    # itera enquanto não acabarem pétalas
    while petalas_qtd > 0:
        data, addr = sock.recvfrom(1024)
        petalas_qtd -= 1 
        
        # lógica
        mensagem = str(petalas_qtd)
        if petalas_qtd % 2 == 0:
            mensagem = "Bem me Quer"
            bem_me_quer = True
        if petalas_qtd % 2 == 1:
            mensagem = "Mal me Quer"
            bem_me_quer = False
        sock.sendto(str.encode(mensagem), addr)
    
    # envia resultado
    if bem_me_quer == True:
        mensagem = "ELE(A) TE AMA!"
    else:
        mensagem = "ELE(A)) NÃO TE AMA!"
    sock.sendto(str.encode(mensagem), addr)
    break