import socket #biblioteca principal para a criacao de envio de sockets ao servidor para obter info de portas.
import threading #importada para o uso de multi threading, acelerar o procesos de busca.
import time #cronometro

thread_limit = threading.Semaphore(value=100) #define o valor limite de thread para rodar ao mesmo tempo. (concorrencia controlada)
    
def scan_port(endereco, porta):
    with thread_limit:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket tipo INET, socket stream
        s.settimeout(2) #tempo de 2 segundos entre buscas
        
        if s.connect_ex((endereco, porta)) == 0: #caso a porta estiver aberta...
            try:
                banner = s.recv(1024).decode().strip() #envia um pacote para tentar obter o serviço
                print(f"[+] Porta {porta} aberta! Serviço: {banner}")  
            except:
                print(f"[+] Porta {porta} aberta! (Serviço desconhecido)")
        s.close() #finaliza o socket para nao acumular.
     
if __name__ == "__main__": #este name main significa para rodar o programa daq para baixo se for executado
    endereco = input("Insira o Endereço: ")
    porta_final = int(input("Insira uma porta limite: "))
    
    tempo_inicial = time.time()
    
    threads = [] #armazena os threads em uma lista
    for porta in range(1, porta_final + 1):
        t = threading.Thread(target=scan_port, args=(endereco, porta)) #threads tem como algo a funcao scan_port com os seguintes argumentos.
        threads.append(t)
        t.start() #comeca o auê
            
    for t in threads:
        t.join() #só acaba quando todos os threads finalizarem!!!
        
    tempo_final = time.time()
    
    duracao = tempo_final - tempo_inicial
        
    print(f"\n[!] Escaneamento concluído em {duracao:.2f} segundos.")
        