import socket
import threading


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.223.233", 12345)

    # Ingresar el nombre de usuario
    user_name = input("Ingresa tu nombre de usuario: ")

    # Conectar al servidor
    client_socket.connect(server_address)

    # Enviar el nombre de usuario al servidor
    client_socket.send(user_name.encode("utf-8"))

    # Iniciar un hilo para recibir mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Enviar mensajes al servidor
    while True:
        user_message = input()
        client_socket.send(user_message.encode("utf-8"))


def receive_messages(socket):
    try:
        while True:
            message = socket.recv(1024).decode("utf-8")
            print(message)
    except Exception as e:
        print(f"Error al recibir mensajes: {e}")


if __name__ == "__main__":
    start_client()
