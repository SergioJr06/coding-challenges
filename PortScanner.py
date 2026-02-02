import socket

endereco = input("Digite o seu endereço para o PortScanner passar as portas abertas!\n")
porta_final = input("Até qual porta você quer tenta?\n")
porta_final = int(porta_final)

for porta in range(1, porta_final + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((endereco, porta)) == 0:
        print(f"A porta {porta} está aberta!")  
    s.close()