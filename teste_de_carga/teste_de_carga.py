import socket        # ultilizar a biblioteca de sockets
import threading    # ultilizar a biblioteca de threads
import time


'''
1. < Teste de Carga >

- Criar um servidor que receba uma requisição e responda com o mesmo conteúdo.
- Ao final do teste, mostrar quantos segundos foram necessários para realizar todas as requisições.
- Obs: Não é preciso criar mais servidores ou clientes, apenas 1 servidor e vários clientes simultâneos.

2. < configurações do servidor >
   - host >> 127.0.0.1
   - porta da thread unica >> 8080
   - porta da thread multipla >> 8081

3. < funções >
   - handle_thread_unica >> função para tratat as requisições no servidor thread_unica.
   - handle_thread_multiplas >> função para tratat as requisições noservidor thread_multiplas.
   - sever_thread_unica >> função para fazer a conecxão do servidor usando thread_unica.
   - server_thread_multiplas >> função para fazer a conecxão do servidor usando thread_multiplas.
   - main >> para execução do codigo.

'''

# configurar servidor
HOST = "127.0.0.1"

# portas diferentes para cada tipo de conexão (thread)
PORT_THREAD_UNICA = 8080
PORT_THREAD_MULTIPLAS = 8081

# função para tratat as requisições no servidor thread_unica


def handle_thread_unica(socket_cliente):
    requisicao = socket_cliente.recv(1024)
    # simulano processamento de requisição
    time.sleep(0.1)
    resposta = b"OK"
    socket_cliente.send(resposta)
    socket_cliente.close()
# funcao para tratar as threds_multiplas


def handle_thread_multiplas(socket_cliente):
    requisicao = socket_cliente.recv(1024)
    # simulano processamento de requisição
    time.sleep(0.1)
    resposta = b"OK"
    socket_cliente.send(resposta)
    socket_cliente.close()

#                     criando servidores

# thread_unica


def sever_thread_unica():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT_THREAD_UNICA))
    serverSocket.listen()
    
    while True:
        socket_cliente, add = serverSocket.accept()
        # chamando a função sem uso de threads
        handle_thread_unica(socket_cliente)

# thread_multiplas


def server_thread_multiplas():
    serverSocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
        )
    serverSocket.bind(
        (HOST, PORT_THREAD_MULTIPLAS)
        )
    serverSocket.listen()
    while True:
        socket_cliente, add = serverSocket.accept()
        thread_cliente = threading.Thread(
            target=handle_thread_multiplas, args=(socket_cliente,)
            )
        thread_cliente.start()


# main
def main():
    # iniciando servidor de multiplas threads
    server_thread_multiplas_thead = threading.Thread(
        target=server_thread_multiplas
        )
    server_thread_multiplas_thead.start()

# iniciando servidor de unica thread
    sever_thread_unica()
    
# aguardando o termmino do servidor de multiplas threads
    server_thread_multiplas_thead.join()



if __name__ == "__main__":
    main()
