import tkinter as tk
import psutil
import matplotlib.pyplot as plt

class RAM:
    def __init__(self):
        self.show_ram_enabled = False
        self.ramButton = None

    def update_ram(self, ram_label, window, graph_label):
        if self.show_ram_enabled:
            memory_info = psutil.virtual_memory()
            ram_label.config(text=f"USED: {memory_info.used/(1024**3):.1f}GB/{memory_info.total/(1024**3):.1f}GB ({memory_info.percent}%)\nAVAILABLE: {memory_info.available/(1024**2):.1f}MB")
            graph_label.config(text = "success")
        window.after(1000, lambda: self.update_ram(ram_label, window,graph_label))

    def show_ram(self, ram_label, window,graph_label):
        self.show_ram_enabled = True
        self.update_ram(ram_label, window,graph_label)  # Start updating RAM when button is pressed

    def ram_btn(self, window, ram_label,graph_label):
        if self.ramButton is None:  # Check if the button exists
            self.ramButton = tk.Button(window, width=7, height=1, text='RAM', borderwidth=2, relief='ridge', 
                                        command=lambda: self.show_ram(ram_label, window,graph_label))
            self.ramButton.grid(row=0, column=1)
        else:
            # If button exists but was hidden, show it again
            self.ramButton.grid(row=0, column=1)

    def remove_ram_btn(self):
        if self.ramButton is not None:
            self.ramButton.grid_forget()  # Hide the button
            self.ramButton = None  # Reset the button reference
    
    
    def elsebtn(self, ram_label, graph_label):
        self.show_ram_enabled = False
        ram_label.config(text="")
        graph_label.config(text="")
        
        self.remove_ram_btn()