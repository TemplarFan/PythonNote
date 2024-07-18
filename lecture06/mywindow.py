from tkinter.colorchooser import *
import tkinter as tk

root = tk.Tk()

def quit():
    ans = askcolor(title="choose color.", color="#fff000")
    if ans:
        print(ans)
        btn.config(bg=ans[1])
    else:
        print("cancel the color selection.")

btn = tk.Button(root, text="HELLO NEU.")
btn.config(bg="yellow", fg="blue")

btn.config(command=quit)

btn.pack(expand=tk.YES, fill=tk.BOTH)
root.geometry("500x300")
root.mainloop()