import socket


SERVER_IP = "localhost" 
# Localhost = 10.220.33.29
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
print(f"Servers started at {SERVER_IP}:{SERVER_PORT}")

def GetPlayerChoice(playerNumber):
    server_socket.listen(1)
    print(f"Waiting for Player {playerNumber} to connect...")

    client_socket, client_address  = server_socket.accept()
    print(f"Player {playerNumber} connected from {client_address}")

    data = client_socket.recv(1024)
    choice = data.decode("utf-8").strip().lower()
    print(f"Player {playerNumber} chose: {choice}")

    return choice

P1 = GetPlayerChoice(1)
P2 = GetPlayerChoice(2)

def RPSLogic(P1, P2):
    if P1 == P2:
        return "Draw"
    elif (P1 == "rock" and P2 == "scissors") or (P1 == "paper" and P2 == "rock") or (P1 == "scissors" and P2 == "paper"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

