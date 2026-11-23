import socket
import threading

SERVER_IP = "localhost" 
# Localhost = 10.220.33.29
SERVER_PORT = 5000

clients = {}
clients.setdefault("")
clients_lock = threading.Lock()

def RPSLogic(P1, P2):
    """Determines the winner of a rock-paper-scissors game based on the choices of two players."""
    if P1 == P2:
        return "Draw"
    elif (P1 == "rock" and P2 == "scissors") or (P1 == "paper" and P2 == "rock") or (P1 == "scissors" and P2 == "paper"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

def broadcast(message, sender_socket=None, blocked = None):
    """Sends a message to all connected clients (optionally skipping the sender)."""
    with clients_lock:
        # Iterate over a shallow copy so we can safely remove disconnected clients
        for client in clients.copy:
            if client != blocked:
                try:
                    client.sendall(message)
                except OSError:
                    # Clean up broken connections
                    client.close()
                    clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with clients_lock:
        clients[conn]
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            clientMessage = data.decode("utf-8")
            if clientMessage[:1] == "$":
                clients[conn] = str(clientMessage[1:])
                for client, v in clients:
                    if (v != "") and (client != conn):
                        returnMessage = RPSLogic(list(clients.keys())[0], list(clients.keys())[1])
                        finishingMessage = f"Player 1 chose: {list(clients.keys())[0]}\nPlayer 2 chose: {list(clients.keys())[1]}\n{returnMessage}\n\nWould you like to play again?: "
                        client.sendall(finishingMessage.encode("utf-8"))

            elif clientMessage[:1] == "%":
                if clientMessage[1:] == "N":
                    conn.close()
                    if conn in clients:
                        clients.pop[conn]
                    break

            # Forward the received message to everyone else
            broadcast(data, sender_socket=conn)
    except ConnectionResetError:
        pass
    finally:
        with clients_lock:
            if conn in clients:
                clients.pop[conn]
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen()
    print(f"[LISTENING] Server running on {SERVER_IP}:{SERVER_PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()

if __name__ == "__main__":
    start_server()