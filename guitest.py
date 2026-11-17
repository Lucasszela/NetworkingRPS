import tkinter as tk


root = tk.Tk()

choice = None

# main window
root.title("Rock Paper Scissors")
root.geometry("300x200")


# what happens when the button is clicked
def button_clicked(value):
    global choice
    choice = value

# text label
label = tk.Label(root, text="Rock Paper Scissors", font =("Arial", 16))
label.pack(pady=20)

# button creation
rock = tk.Button(root, text="Rock", command=lambda: button_clicked("rock"))
rock.pack(pady=5)
paper = tk.Button(root, text="Paper", command=lambda: button_clicked("paper"))
paper.pack(pady=5)
scissors = tk.Button(root, text="Scissors", command=lambda: button_clicked("scissors"))
scissors.pack(pady=5)


root.mainloop()