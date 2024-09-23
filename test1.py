import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import time

class RAMUsageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RAM Usage Monitor")

        self.frame = tk.Frame(root)
        self.frame.pack()

        # Create a Matplotlib figure
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("RAM Usage Percentage")
        self.ax.set_ylim(0, 100)
        self.x_data = []
        self.y_data = []

        # Create a canvas to hold the figure
        self.graph_label = tk.Label(self.frame, text="Press 'Update Graph' to see RAM usage.")
        self.graph_label.grid(row=0, column=0)
        # Start updating the plot
        self.update_plot()

    def update_plot(self,graph_label):
        # Get RAM usage percentage
        ram_usage = psutil.virtual_memory().percent

        # Update data lists
        self.x_data.append(time.time())
        self.y_data.append(ram_usage)

        # Clear the axes and plot the new data
        self.ax.clear()
        self.ax.set_title("RAM Usage Percentage")
        self.ax.set_ylim(ram_usage-5, ram_usage+5)
        self.ax.plot(self.x_data, self.y_data, label=f'RAM Usage ({ram_usage}%)', color='blue')
        self.ax.legend()
        self.ax.grid()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_label)
        self.canvas.get_tk_widget().grid(row=1, column=0)
        # Refresh the canvas
        self.canvas.draw()
        
        # Schedule the next update
        self.root.after(1000, self.update_plot)  # Update every second

# Create the main window
root = tk.Tk()
app = RAMUsageApp(root)
root.mainloop()
