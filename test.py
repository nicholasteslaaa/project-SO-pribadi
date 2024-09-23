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
        self.frame.grid(row=0, column=0)

        # Label for displaying the graph
        self.graph_label = tk.Label(self.frame, text="Press 'Update Graph' to see RAM usage.")
        self.graph_label.grid(row=0, column=0)

        # Button to update the graph
        self.update_button = tk.Button(root, text="Update Graph", command=self.update_plot)
        self.update_button.grid(row=1, column=0)

    def update_plot(self):
        # Create a new Matplotlib figure
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("RAM Usage Percentage")
        self.ax.set_ylim(0, 100)

        # Get RAM usage percentage
        ram_usage = psutil.virtual_memory().percent

        # Plot the data
        self.ax.clear()
        self.ax.set_title("RAM Usage Percentage")
        self.ax.set_ylim(0, 100)
        self.ax.bar(['RAM Usage'], [ram_usage], color='blue')  # Display as a bar graph
        self.ax.grid()

        # Create a canvas to hold the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_label)
        self.canvas.get_tk_widget().grid(row=1, column=0)

        # Refresh the canvas
        self.canvas.draw()

# Create the main window
root = tk.Tk()
app = RAMUsageApp(root)
root.mainloop()
