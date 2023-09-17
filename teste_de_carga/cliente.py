import socket
import threading
import time


'''
1. < configurando clliente >
    - host >> local host
    - porta da thread unica >> 8080
    - porta da thread multipla >> 8081
    - num de requisições para teste de carga >> 100

2. < requisicoes_cliente >
- envia uma mensagem ao servidor e espera por resposta, caso a mesma seja recebida o cliente finaliza sua execução
- envia uma mensagem ao servidor, espera resposta e imprime o tempo gasto na tela
- repete esse processo quantas vezes foram informadas no parametro 'num'
- fecha a conexão com o cliente após terminar as requisiçoes

3. < respostas_servidor >
4. < servidor >
5. < cliente >
6. < analise dos resultados >
7. < conclusao do projeto >


'''
HOST = 'localhost'  # localhost, ip do computador que esta rodando o script

# portas diferentes para cada tipo de conexão (thread)
PORT_THREAD_UNICA = 8080
PORT_THREAD_MULTIPLAS = 8081

# numero de requisições

NUM_REQUISICOES = 100
# funçao parar tratar as requisições dos testes de cargas


def requisicoes_cliente(server_port):

    client = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM
    )

    client.connect(
        (HOST, server_port)
    )

    request = b"ADD;10;11"  # Exemplo de requisição
    client.send(request)
    response = client.recv(1024)
    client.close()
    return response


def main():

    # tratando as reqisições da thread unica.
    start_time = time.time()

    # Crie 100 clientes para o servidor thread unica
    for _ in range(NUM_REQUISICOES):
        client_response = requisicoes_cliente(PORT_THREAD_UNICA)
        # Processar a resposta, se necessário

    singlethread_time = time.time() - start_time
    print(
        f"Tempo total para servidor singlethread: {singlethread_time:.2f} segundos"
        )

    # tratando as reqisições da thread multiplas
    start_time = time.time()

    # Crie 100 clientes para o servidor multithread
    for _ in range(NUM_REQUISICOES):
        client_response = requisicoes_cliente(PORT_THREAD_MULTIPLAS)
        # Processar a resposta, se necessário

    multithread_time = time.time() - start_time
    print(
        f"Tempo total para servidor multithread: {multithread_time:.2f} segundos"
        )
    

if __name__ == "__main__":
    main()