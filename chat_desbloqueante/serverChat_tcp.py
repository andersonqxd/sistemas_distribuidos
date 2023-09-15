import socket
import threading

HOST = "127.0.0.1"
PORT = 5432

# Lista para armazenar conexções dos clientees
clientes = []

# Funçao para lidar com as conexões com os clients
def identificando_cliente(cliente_socket):
    while True:
        try:
            # Receber a mensagem do cliente
            data = cliente_socket.recv(1024).decode('utf-8')
            print(data)
            if not data:
                break 

            for client in clientes:
               if client != cliente_socket:
                    try:
                        client.send(data.decode('utf-8'))
                    
                    except:
                        clientes.remove
        except:
            pass

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor de chat escutando em {HOST}:{PORT}")

    while True:
        cliente_socket, addr = server.accept()
        clientes.append(cliente_socket)

        chat_client = threading.Thread(target=identificando_cliente, args=(cliente_socket,))
        chat_client.start()

        while True:
            menssagem = input()
            cliente_socket.send(menssagem.encode('utf-8'))
        

if __name__ == "__main__":
    main()





