import socket
import threading


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("192.168.223.233", 12345)

    # Ingresar el nombre de usuario
    user_name = input("Ingresa tu nombre de usuario: ")

    # Enviar el nombre de usuario al servidor
    send_command(f"/name {user_name}", client_socket, server_address)

    # Iniciar un hilo para recibir mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Enviar mensajes al servidor
    while True:
        user_message = input()
        send_command(user_message, client_socket, server_address)


def receive_messages(socket):
    while True:
        data, _ = socket.recvfrom(1024)
        message = data.decode("utf-8")
        print(message)


def send_command(command, socket, server_address):
    try:
        socket.sendto(command.encode("utf-8"), server_address)
    except Exception as e:
        print(f"Error al enviar comando: {e}")


if __name__ == "__main__":
    start_client()
