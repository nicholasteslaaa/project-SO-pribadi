import tkinter as tk
from performances import RAM

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x300")
    
    performance_instance = RAM()  # Create an instance

    left_label = tk.Label(window, width=10, text="Project SO", font=("Arial", 12))
    left_label.grid(row=0, column=0)

    ram_label = tk.Label(window, width=25, height=4)
    ram_label.grid(row=1, column=1,columnspan=10,rowspan=1,pady=1,padx=1)
    
    graph_label = tk.Label(window, width=10,height=2,text="-")
    graph_label.grid(row=3, column=1,columnspan=10,rowspan=1,pady=1,padx=1)
    
    
    performances_btn = tk.Button(window, width=12, height=2, text="Performances", borderwidth=2, relief="solid",
                                 command=lambda: performance_instance.ram_btn(window,ram_label,graph_label))
    performances_btn.grid(row=1, column=0)

    else_btn = tk.Button(window, width=12, height=2, text="Else", borderwidth=2, relief="solid",
                         command=lambda: performance_instance.elsebtn(ram_label,graph_label))
    else_btn.grid(row=2, column=0)

    window.mainloop()
