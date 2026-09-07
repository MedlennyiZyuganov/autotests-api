import socket
import threading

history = []

def client_address(conn, addr):
    print(f"Пользователь с адресом: {addr} подключился к серверу")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode().strip()
            print(f"Пользователь с адресом: {addr} отправил сообщение: {message}")


            history.append(message)


            response = "\n".join(history)
            conn.sendall(response.encode())
    except Exception as e:
        print(f"Ошибка соединения {addr}: {e}")
    finally:
        conn.close()
        print(f"Соединение прервано: {addr}")

def start_server(host='localhost', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Сервер запущен на {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_address, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()