import tkinter as tk
from itertools import count
def start_counter(label):
    counter = count(0)
    def update_func():
        label.config(text=str(counter.__next__()))
        label.after(1000, update_func)
    update_func()

root = tk.Tk()
root.title("Counting Seconds")

label = tk.Label(root, fg="red")
label.pack()

start_counter(label)

button = tk.Button(root, text='Stop', width=30, command=root.destroy)
button.pack()

root.mainloop()
