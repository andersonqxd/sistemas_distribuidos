import socket
import threading

HOST = "127.0.0.1"
PORT = 5432
print("Bate-papo")

def receive_messages(cliente_socket):
    while True:
         try:
            data = cliente_socket.recv(1024).decode('utf-8')
            print(data)
         except:
            break

def main():
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect((HOST, PORT))

   receive_thread = threading.Thread(target=receive_messages, args=(client,))
   receive_thread.start()

   while True:
      menssagem = input()
      if menssagem != "tchau" or "xau":
         client.send(menssagem.encode('utf-8'))
      else:
       break

if __name__ == "__main__":
    main()
        
