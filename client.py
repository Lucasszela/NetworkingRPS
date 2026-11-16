import socket
import time
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

choice = ""
choices = ["rock", "paper", "scissors"]

def choose():
    choiceInt = str(input("Please choose the number of the option you want to select:\n\n(1) Rock\n(2) Paper\n(3) Scissors\n\n"))
    if choiceInt == "1":
        choice = "rock"
    elif choiceInt == "2":
        choice = "paper"
    elif choiceInt == "3":
        choice = "scissors"
    else:
        choice = random.choice(choices)

def main():

    serverAddress = "";
    serverPort = 0;

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.settimeout(1.0)

    print(f"Pinging {serverAddress}:{serverPort}:\n")


if __name__ == "__main__":
    main()