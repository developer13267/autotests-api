import socket

users_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

users_server_address = ('localhost', 12345)
users_client_socket.connect(users_server_address)

message = "Привет?!"
users_client_socket.send(message.encode())
response = users_client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

users_client_socket.close()