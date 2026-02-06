import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

class ECG_GUI:
    def __init__(self):
        #properies of the window screen 
        self.window = tk.Tk()
        self.window.title("CSV Ploter")
        self.window.geometry("400x300")

        #Labels to fil out the boxes 
        tk.Label(self.window, text="CSV File").pack()
        self.file_entry = tk.Entry(self.window)
        self.file_entry.pack()

        #the entry boxs(user input)labels both for Y and X ax
        tk.Label(self.window, text="X Column").pack()
        self.x_entry = tk.Entry(self.window)
        self.x_entry.pack()

        tk.Label(self.window, text="Y Column").pack()
        self.y_entry = tk.Entry(self.window)
        self.y_entry.pack()

        #clickabe botten for user to click when user wants to create plot
        tk.Button(self.window, text="Plot ECG", command=self.plot_ecg).pack(pady=10)

    def plot_ecg(self):
        #Reading user input
        file = self.file_entry.get()
        x_col = self.x_entry.get()
        y_col = self.y_entry.get()

        #grabing file rwading data
        data = pd.read_csv(file)

        #ploting data
        plt.plot(data[x_col], data[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title("ECG Signal")
        plt.show()

gui = ECG_GUI()
gui.window.mainloop()
