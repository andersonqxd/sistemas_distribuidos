import socket

HOST = "127.0.0.1"
PORT = 65432
print("chat:")
while True:
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk_Client:
        
        mensagem = input()
        sk_Client.connect((HOST, PORT))
        sk_Client.sendall(mensagem.encode('utf-8'))
        result_Encode = sk_Client.recv(1024)
        result_Decode = result_Encode.decode('utf-8')
        print(result_Decode,"\n")


