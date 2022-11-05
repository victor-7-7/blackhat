import socket

HOST = 'www.google.com'
PORT = 80

# создаем объект сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаем клиент
client.connect((HOST, PORT))
# отправляем какие-нибудь данные
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
# принимаем какие-нибудь данные
response = client.recv(4096)

print(response.decode('utf-8'))
client.close()

