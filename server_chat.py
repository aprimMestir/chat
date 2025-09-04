import socket
import threading

#Настройки сети
HOST = "0.0.0.0"
# для прослушивания всех интерфейсов
PORT = 5050
######################################
clients = []
def client(conn, addr):
    print(f"Подключился {addr}")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = f"{addr}:{data.decode()}"
            print(message)
            for client in clients:
                if clients != conn:
                    client.sendall(message.encode())
        except:
            break
    print(f"[-] Отключился {addr}")
    clients.remove(conn)
    conn.close()



def server_start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()
    print(f"[SERVER] Сервер запущен на {HOST}:{PORT}")

    while True:
        conn,addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=client, addr=(conn, addr))
        thread.start()

if __name__=="__main__":
    server_start()
