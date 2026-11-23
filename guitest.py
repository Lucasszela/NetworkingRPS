import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()  # create the main window


choice = None
buttons = []  

# main window
root.title("Rock Paper Scissors")
root.geometry("450x300")


# what happens when the button is clicked
def button_clicked(value):
    global choice
    choice = value
    label.configure(text=f"You chose: {choice} waiting for opponent...")
    for button in buttons:
        button.configure(state="disabled")  # disable all buttons after a choice is made
    
# text label
label = ctk.CTkLabel(root, text="Choose an option", font=("Arial", 16))
label.pack(pady=20)

# button creation
for choice in ["Rock", "Paper", "Scissors"]:
    button = ctk.CTkButton(root, text=choice, command=lambda c=choice: button_clicked(c))
    button.pack(pady=5)
    buttons.append(button)

root.mainloop()