import socket

def users_server():
    users_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    users_server_address = ('localhost', 12345)
    users_server_socket.bind(users_server_address)

    users_server_socket.listen(10)
    print("Сервер запущен и ждет подключений..")
    logs_massage = []

    while True:
        users_client_socket, users_client_address = users_server_socket.accept()
        print(f"Пользователь с адресом: {users_client_address} подключился к серверу")
        users_data = users_client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {users_client_address} отправил сообщение: {users_data}")
        logs_massage.append(users_data)

        response = '\n'.join(logs_massage)
        users_client_socket.send(response.encode())



        users_client_socket.close()
if __name__ == '__main__':
    users_server()