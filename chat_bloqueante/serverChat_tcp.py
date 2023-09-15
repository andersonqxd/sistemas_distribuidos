import socket
from chat import chat

HOST = "127.0.0.1"
PORT = 65432

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.bind((HOST, PORT))
        sk.listen()
        conn, addr = sk.accept()
        with conn:
            print("conectado a: ", addr )
            data = conn.recv(1024)
            informacao = data.decode("utf-8")
            if informacao == "tchau":
                break
            else:
               print(informacao)
               resposta = chat.mensagem()
               conn.send(resposta.encode('utf-8'))
