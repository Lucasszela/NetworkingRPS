import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()  # create the main window


choice = None

# main window
root.title("Rock Paper Scissors")
root.geometry("450x300")


# what happens when the button is clicked
def button_clicked(value):
    global choice
    choice = value
    label.configure(text=f"You chose: {choice} waiting for opponent...")

# text label
label = ctk.CTkLabel(root, text="Choose an option", font=("Arial", 16))
label.pack(pady=20)

# button creation
rock = ctk.CTkButton(root, text="Rock", command=lambda: button_clicked("rock"))
rock.pack(pady=5)
paper = ctk.CTkButton(root, text="Paper", command=lambda: button_clicked("paper"))
paper.pack(pady=5)
scissors = ctk.CTkButton(root, text="Scissors", command=lambda: button_clicked("scissors"))
scissors.pack(pady=5)


root.mainloop()