import socket

host = 'localhost'
port = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Подключено к серверу.")

    try:
        while True:
            message = input("Ваше сообщение: ")
            if message.lower() in ("exit", "quit"):
                break

            client.sendall(message.encode())

            data = client.recv(1024)
            response = data.decode()
            print(response)
    finally:
        client.close()
        print("Соединение закрыто.")

if __name__ == "__main__":
    main()