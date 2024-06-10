import string
import random
from tkinter import *
import customtkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image


def generate_password():
    global password_generated 
    try:
        length = int(entry.get())
        if length < 8:
            messagebox.showinfo("WARNING!", "Your password length is small!")
            return
        if length > 100:
            messagebox.showinfo("WARNING!", "Your password length is long!")
            return
    except ValueError:
        messagebox.showinfo("WARNING!", "Please, enter numbers only.")
        return
    
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    
    characters = s1 + s2 + s3 + s4
    
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    final_password = "".join(password)
    
    label.configure(text=final_password)
    password_generated = True

def copy_to_clipboard():
    if password_generated:
        password = label.cget("text")
        win.clipboard_clear()
        win.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showinfo("WARNING!", "Generate a password first.")

customtkinter.set_appearance_mode("System")
win = customtkinter.CTk()
win.title("Password Generator")
win.geometry("500x500")
win.resizable(False, False)

label = customtkinter.CTkLabel(win, text="", font=("Arial", 24), wraplength=480, justify="center")
label.pack(pady=60)

entry = customtkinter.CTkEntry(win, width=60)
entry.focus_set()
entry.pack()

customtkinter.CTkButton(win, fg_color="#FF785A", hover_color="#D5634A", text_color="black", text="Generate Password", font=("Arial", 18), width=20, command=generate_password).pack(pady=20)
customtkinter.CTkButton(win, fg_color="#FF785A", hover_color="#D5634A", text_color="black", text="Copy to Clipboard", font=("Arial", 18), width=20, command=copy_to_clipboard).pack(pady=20)

password_generated = False

win.mainloop()
