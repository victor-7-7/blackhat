import socket
import threading

IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Сервер будет прослушивать порт PORT по адресу IP
    server.bind((IP, PORT))
    # Начинаем слушать. Отложенных соединений должно быть не больше 5
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # При подключении очередного клиента получаем его данные
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # Создаем поток-хэндлер для взаимодействия с клиентом
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # Запускаем этот поток
        client_handler.start()
        # В этой точке главный цикл сервера освобождается для обработки
        # следующего входящего соединения


def handle_client(client_socket):
    with client_socket as sock:
        # Получаем клиентский запрос
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        # Возвращаем клиенту некий ответ
        sock.send(b'ACKKK')


if __name__ == '__main__':
    main()
