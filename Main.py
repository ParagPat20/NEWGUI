import tkinter as tk
from login import loginWindow
from MainWindow import mainWindow

root = tk.Tk()
root.withdraw()

if __name__ == "__main__":

    # loginWindow()
    mainWindow()

    root.mainloop()