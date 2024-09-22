import tkinter as tk
import psutil

# Global flag to track if the RAM display is enabled
show_ram_enabled = False

def update_ram():
    if show_ram_enabled:
        memory_info = psutil.virtual_memory()
        ram_label.config(text=f"Memory Usage: {memory_info.percent}%")
    window.after(1000, update_ram)  # Check again after 1 second

def show_ram():
    global show_ram_enabled
    show_ram_enabled = True

def elsebtn():
    global show_ram_enabled
    show_ram_enabled = False
    ram_label.config(text="")

window = tk.Tk()
window.geometry("600x300")

left_label = tk.Label(window, width=10, text="Project SO", font=("Arial", 12))
left_label.grid(row=0, column=0)

ram_label = tk.Label(window, width=20, height=5, text='RAM Usage: 0%')
ram_label.grid(row=1, column=1)

performances_btn = tk.Button(window, width=12, height=2, text="Performances", borderwidth=2, relief="solid", command=show_ram)
performances_btn.grid(row=1, column=0)

else_btn = tk.Button(window, width=12, height=2, text="Hide RAM", borderwidth=2, relief="solid", command=elsebtn)
else_btn.grid(row=2, column=0)

update_ram()

window.mainloop()
