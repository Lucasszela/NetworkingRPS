import socket


SERVER_IP = "localhost"
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
print(f"Servers started at {SERVER_IP}:{SERVER_PORT}")

server_socket.listen(1)
print("Server listening for connections")

def RPSLogic(P1, P2):
    if P1 == P2:
        return "Draw"
    elif (P1 == "rock" and P2 == "scissors") or (P1 == "paper" and P2 == "rock") or (P1 == "scissors" and P2 == "paper"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

