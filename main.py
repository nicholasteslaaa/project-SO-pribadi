import tkinter as tk
import psutil


class performances():
    show_ram_enabled = False
    ramButton = None
    def update_ram():
        if performances.show_ram_enabled==True:
            memory_info = psutil.virtual_memory()
            ram_label.config(text=f"{memory_info.percent}%")
        window.after(1000,performances.update_ram)
        
    def show_ram():
        global show_ram_enabled
        performances.show_ram_enabled = True
        
    def ram_btn():
        if performances.ramButton is None:  # Check if the button exists
            performances.ramButton = tk.Button(window, width=7, height=1, text='ram', borderwidth=2, relief='ridge', command=performances.show_ram)
            performances.ramButton.grid(row=0, column=1)
        else:
            # If button exists but was hidden, show it again
            performances.ramButton.grid(row=0, column=1)
            
    def remove_ram_btn():
        if performances.ramButton is not None:
            performances.ramButton.grid_forget()  # Hide the button
        
    def elsebtn():
        global show_ram_enabled
        performances.show_ram_enabled = False
        ram_label.config(text="")
        performances.remove_ram_btn()


window = tk.Tk()
window.geometry("600x300")
performances.update_ram()

left_label = tk.Label(window,width=10,text="Project SO",font=("Arial",12))
left_label.grid(row=0,column=0)

ram_label= tk.Label(window,width=10,height=5,text='ram')
ram_label.grid(row=1,column=1)

performances_btn = tk.Button(window,width=12,height=2,text="Performances",borderwidth=2, relief="solid", command=performances.ram_btn)
performances_btn.grid(row=1,column=0)

else_btn = tk.Button(window,width=12,height=2,text="else",borderwidth=2, relief="solid", command=performances.elsebtn)
else_btn.grid(row=2,column=0)


window.mainloop()