import socket          # библиотека для сети
import threading       # библиотека для многопоточности

HOST = "127.0.0.1"     # IP сервера (127.0.0.1 = локальный компьютер)
PORT = 5000            # порт сервера

# Функция для приёма сообщений от сервера
def receive(sock):
    while True:
        try:
            data = sock.recv(1024)          # ждём сообщение от сервера
            if not data:                    # если сервер закрыл соединение
                break
            print("\n" + data.decode() + "\n> ", end="")
            # выводим сообщение и снова показываем ">" для ввода
        except:
            break                           # ошибка -> выходим из цикла

# Основная функция клиента
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём TCP-сокет
    sock.connect((HOST, PORT))   # подключаемся к серверу

    print("Подключено к чату. Пишите сообщения:")

    # запускаем поток для приёма сообщений от сервера
    thread = threading.Thread(target=receive, args=(sock,))
    thread.daemon = True         # поток завершается вместе с программой
    thread.start()

    # бесконечный цикл для отправки сообщений
    while True:
        msg = input("> ")        # ждём ввод пользователя
        if msg.lower() == "exit": # если ввели "exit" — выходим
            break
        sock.sendall(msg.encode())  # отправляем сообщение на сервер

    sock.close()  # закрываем соединение

if __name__ == "__main__":
    main()        # запуск клиента
