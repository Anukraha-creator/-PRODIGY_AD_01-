import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")
    else:
        current = screen.get()
        screen.set(current + text)

root = tk.Tk()
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold", bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20, font="Arial 18 bold")
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
