import socket
from interface import interface


def conectCalc(HOST, PORT):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk_Client:
        sk_Client.connect((HOST, PORT))

        expressao = interface.menu()

        sk_Client.sendall(expressao.encode('utf-8'))
        result_Encode = sk_Client.recv(1024)
        
        result_Decode = result_Encode.decode('utf-8')
        print("Resultado da operação:",result_Decode,"\n")

def desconectCalc(HOST, PORT):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk_Client:
        sk_Client.connect((HOST, PORT))
        expressao = "nao"

        sk_Client.sendall(expressao.encode('utf-8'))
        result_Encode = sk_Client.recv(1024)
        
        result_Decode = result_Encode.decode('utf-8')
        print("OK, até logo!!!")
    

#INTERFACE DE  LOOPBACK -> (localhost)
HOST = "127.0.0.1"
# PORTA DO LISTEN  
PORT = 65432

teste = True
while teste:
    escolha = input("deseja fazer uma operação matematica sim ou nao: ")
    if escolha == "sim":
        conectCalc(HOST, PORT)
    else:
        desconectCalc(HOST, PORT)
        break
    
   

