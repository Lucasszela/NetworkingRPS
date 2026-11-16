import socket
import time
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    serverAddress = "";
    serverPort = 0;

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.settimeout(1.0)

    print(f"Pinging {serverAddress}:{serverPort}:\n")


if __name__ == "__main__":
    main()