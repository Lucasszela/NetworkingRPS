import socket
import time
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

choice = ""
choices = ["rock", "paper", "scissors"]
repeat = True

def choose():
    choiceInt = str(input("Please choose the number of the option you want to select:\n\n(1) Rock\n(2) Paper\n(3) Scissors\n\n"))
    if choiceInt == "1":
        return "rock"
    elif choiceInt == "2":
        return "paper"
    elif choiceInt == "3":
        return "scissors"
    else:
        return random.choice(choices)

def main():
    global repeat
    while repeat == True:
        serverAddress = "10.220.33.29" #lucas laptop
        serverPort = 5000

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(1.0)

        print(f"Pinging {serverAddress}:{serverPort}:\n")

        choice = choose()

        try:
<<<<<<< HEAD
            # debug
            clientSocket.sendto(choice.encode("utf-8"), (serverAddress, serverPort))
            response, serverAddress = clientSocket.recvfrom(1024)
=======
            clientSocket.connect((serverAddress, serverPort))
            clientSocket.sendall(choice.encode("utf-8"))
            response = clientSocket.recv(1024)
>>>>>>> f50f1a3cb7465941a5d632f63af480ce5694db97
            print(f"SERVER: {response.decode("utf-8")}")
            repeatPrompt = str(input(""))
            if repeatPrompt == ("Y" or "y"):
                clientSocket.sendto("%Y".encode("utf-8"), (serverAddress, serverPort))
                pass
            else:
                repeat = False

        except socket.timeout:
            print("Request timed out.\n")

    clientSocket.close()


if __name__ == "__main__":
    main()