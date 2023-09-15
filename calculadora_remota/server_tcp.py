import socket
from calculadora import calculadora 
#INTERFACE DE  LOOPBACK -> (localhost)
HOST = "127.0.0.1"
# PORTA DO LISTEN  
PORT = 65432


# socket.AF_INET  -> familia de endereço IPV4
# socket.SOCK_STREAM -> tipo do protocolo TCP 
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk: # with -> intrução usada para para garantir que  o socket seja fehado no final da intrução

        print("socket criado!!")
        sk.bind(( HOST, PORT) ) # usado para associar o socket a uma interface de rede expecifica e uma porta.
        sk.listen()
        conn, addr = sk.accept()
        with conn: # conn -> objeto de conexão do secket 
            print('Connected by',addr)
            data = conn.recv(1024)
            informacao = data.decode('utf-8')
            if informacao == "nao":
                break
            else:     
                valores = informacao.split()

                value1 = int(valores[1])
                value2 = int(valores[2])
                operando = valores[0] 

                
                        
                resultadoFinal = calculadora.calc(operando, value1, value2)
                conn.send(resultadoFinal.encode('utf-8')) 
            

