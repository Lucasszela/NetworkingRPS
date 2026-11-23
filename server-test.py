import socket
import threading

SERVER_IP = "localhost" 
# Localhost = 10.220.33.29
SERVER_PORT = 5000

clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """Sends a message to all connected clients (optionally skipping the sender)."""
    with clients_lock:
        # Iterate over a shallow copy so we can safely remove disconnected clients
        for client in clients[:]:
            if client != sender_socket:
                try:
                    client.sendall(message)
                except OSError:
                    # Clean up broken connections
                    client.close()
                    clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with clients_lock:
        clients.append(conn)
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Forward the received message to everyone else
            broadcast(data, sender_socket=conn)
    except ConnectionResetError:
        pass
    finally:
        with clients_lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()

if __name__ == "__main__":
    start_server()