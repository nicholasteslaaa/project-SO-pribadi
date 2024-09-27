import psutil,os,time,tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Performances_stat:
    def __init__(self):
        self.show_ram_enabled = False
        self.ramButton = None
        
        self.show_cpu_enabled = False
        self.cpuButton = None
        
        # Initialize Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = None
        
        # Data lists for line plots
        self.ram_time_data = []
        self.ram_usage_data = []
        
        self.cpu_time_data = []
        self.cpu_usage_data = []
        
        self.start_time = time.time()

    ############### RAM ###############
    def performances_btn(self, window, performances_label, graph_label):
        self.ram_btn(window, performances_label, graph_label)
        self.cpu_btn(window, performances_label, graph_label)

    def update_ram(self, performances_label, window, graph_label):
        if self.show_ram_enabled:
            memory_info = psutil.virtual_memory()
            performances_label.config(
                text=f"USED: {memory_info.used/(1024**3):.1f}GB/{memory_info.total/(1024**3):.1f}GB ({memory_info.percent}%)\nAVAILABLE: {memory_info.available/(1024**2):.1f}MB"
            )
            current_time = time.time() - self.start_time
            
            if len(self.ram_usage_data) > 5:
                self.ram_usage_data.pop(0)
            else: 
                self.ram_usage_data.append(memory_info.percent)
            
            if len(self.ram_time_data) > 5:
                self.ram_time_data.pop(0)
            else:
                self.ram_time_data.append(current_time)

            self.update_graph(graph_label, self.ram_time_data, self.ram_usage_data, "RAM")
        window.after(1000, lambda: self.update_ram(performances_label, window, graph_label))

    def show_ram(self, performances_label, window, graph_label):
        self.show_ram_enabled = True
        self.show_cpu_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        self.update_ram(performances_label, window, graph_label)

    def ram_btn(self, window, performances_label, graph_label):
        if self.ramButton is None:  # Check if the button exists
            self.ramButton = tk.Button(window, width=7, height=1, text='RAM', borderwidth=2, relief='ridge', 
                                        command=lambda: self.show_ram(performances_label, window, graph_label))
            self.ramButton.grid(row=0, column=1)
        else:
            self.ramButton.grid(row=0, column=1)

    def remove_ram_btn(self):
        if self.ramButton is not None:
            self.ramButton.grid_forget()  # Hide the button
            self.ramButton = None  # Reset the button reference

    ############### CPU ###############
    def cpu_btn(self, window, performances_label, graph_label):
        if self.cpuButton is None:  # Check if the button exists
            self.cpuButton = tk.Button(window, width=7, height=1, text='CPU', borderwidth=2, relief='ridge', 
                                        command=lambda: self.show_cpu(performances_label, window, graph_label))
            self.cpuButton.grid(row=0, column=2)
        else:
            self.cpuButton.grid(row=0, column=2)
    
    def show_cpu(self, performances_label, window, graph_label):
        self.show_cpu_enabled = True
        self.show_ram_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        self.update_cpu(performances_label, window, graph_label)
        
    def update_cpu(self, performances_label, window, graph_label):
        if self.show_cpu_enabled:
            cpu_percent = psutil.cpu_percent(interval=0)
            cpu_freq = psutil.cpu_freq()
            current_freq_ghz = cpu_freq.current / 1000
            cpu_info = os.popen("wmic cpu get Name").read()
            performances_label.config(text=f"CPU: {cpu_info.strip().splitlines()[-1]}\nCPU Usage: {cpu_percent}%\nSpeed: {current_freq_ghz:.2f}GHz")
            
            current_time = time.time() - self.start_time
            if len(self.cpu_usage_data) > 5:
                self.cpu_usage_data.pop(0)
            else: 
                self.cpu_usage_data.append(cpu_percent)
            
            if len(self.cpu_time_data) > 5:
                self.cpu_time_data.pop(0)
            else:
                self.cpu_time_data.append(current_time)
                

            self.update_graph(graph_label, self.cpu_time_data, self.cpu_usage_data, "CPU")
        window.after(1000, lambda: self.update_cpu(performances_label, window, graph_label))

    def remove_cpu_btn(self):
        if self.cpuButton is not None:
            self.cpuButton.grid_forget()  # Hide the button
            self.cpuButton = None  # Reset the button reference

    ############### GRAPH UPDATE ###############
    def update_graph(self, graph_label, time_data, usage_data, label):
        self.ax.clear()  # Clear the previous graph
        self.ax.set_title(f"{label} Usage Over Time")
        self.ax.set_xlabel("Time (seconds)")
        self.ax.set_ylabel(f"{label} Usage (%)")
        
        below , above = None, None
        if self.show_cpu_enabled:
            below , above = 0, 100
        if self.show_ram_enabled:
            if usage_data[-1]-5 < 0:
                below = 0
            if usage_data[-1]+5 > 100:
                above = 100
            else:
                below,above = usage_data[-1]-5, usage_data[-1]+5
            
        self.ax.set_ylim(below,above)
        self.ax.plot(time_data, usage_data, color='blue')
        self.ax.grid(True)

        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.fig, master=graph_label)
            self.canvas.get_tk_widget().grid(row=2, column=1, columnspan=10, rowspan=1, pady=1, padx=1)
        
        self.canvas.draw()  # Update the canvas with the new plot

    ############### ELSE BUTTON ###############
    def elsebtn(self, performances_label, graph_label):
        self.show_ram_enabled = False
        self.show_cpu_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        self.remove_ram_btn()
        self.remove_cpu_btn()
        
        # Clear the graph by destroying the canvas widget
        if self.canvas is not None:
            self.canvas.get_tk_widget().grid_forget()  # Hide the canvas from the grid
            self.canvas.get_tk_widget().destroy()  # Destroy the canvas widget
            self.canvas = None  # Reset the canvas reference