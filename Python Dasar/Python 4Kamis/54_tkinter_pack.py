import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="label 1")
label.pack()

button = tk.Button(root, text="tombol 1")
button.pack()

checkbox = tk.Checkbutton(root, text="centang 1")
checkbox.pack()
tk.mainloop()
root.mainloop()