import socket
import threading
import time

thread_limit = threading.Semaphore(value=100) #define o valor limite de thread para rodar ao mesmo tempo. (concorrencia controlada)
    
def scan_port(endereco, porta):
    with thread_limit:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        if s.connect_ex((endereco, porta)) == 0:
            print(f"[+] Porta {porta} aberta!")  
        s.close()
     
if __name__ == "__main__": #este name main significa para rodar o programa daq para baixo se for executado
    endereco = input("Insira o Endereço: ")
    porta_final = int(input("Insira uma porta limite: "))
    
    tempo_inicial = time.time()
    
    threads = []
    for porta in range(1, porta_final + 1):
        t = threading.Thread(target=scan_port, args=(endereco, porta))
        threads.append(t)
        t.start()
            
    for t in threads:
        t.join()
        
    tempo_final = time.time()
    
    duracao = tempo_final - tempo_inicial
        
    print(f"\n[!] Escaneamento concluído em {duracao:.2f} segundos.")
        