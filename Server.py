import socket


SERVER_IP = "localhost"
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))
print(f"Servers started at {SERVER_IP}:{SERVER_PORT}")