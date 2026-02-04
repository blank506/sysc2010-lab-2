import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

class ECG_GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ECG Viewer")
        self.window.geometry("400x300")

        tk.Label(self.window, text="CSV File").pack()
        self.file_entry = tk.Entry(self.window)
        self.file_entry.pack()

        tk.Label(self.window, text="X Column").pack()
        self.x_entry = tk.Entry(self.window)
        self.x_entry.pack()

        tk.Label(self.window, text="Y Column").pack()
        self.y_entry = tk.Entry(self.window)
        self.y_entry.pack()

        tk.Button(self.window, text="Plot ECG", command=self.plot_ecg).pack(pady=10)

    def plot_ecg(self):
        file = self.file_entry.get()
        x_col = self.x_entry.get()
        y_col = self.y_entry.get()

        data = pd.read_csv(file)

        plt.plot(data[x_col], data[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title("ECG Signal")
        plt.show()

gui = ECG_GUI()
gui.window.mainloop()
