import tkinter as tk

def hide_button():
    button.pack_forget()  # Hides the button

root = tk.Tk()

button = tk.Button(root, text="Click to Hide", command=hide_button)
button.pack()

root.mainloop()
