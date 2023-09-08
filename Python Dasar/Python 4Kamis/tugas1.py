import tkinter as tk
from tkinter import ttk

def hitung():
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())

    hasil = angka1 * angka2

    hasil_var.set(f"Total Rp: {hasil:.2f}")

window = tk.Tk()
window.title("Kalkulator")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

angka1_label = ttk.Label(input_frame, text="Harga : ")
angka1_label.grid(row=0, column=0, sticky="W")
angka1_entry = ttk.Entry(input_frame)
angka1_entry.grid(row=0, column=1)

angka2_label = ttk.Label(input_frame, text="Kuantitas : ")
angka2_label.grid(row=1, column=0, sticky="W")
angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

hitung_button = ttk.Button(window, text="hitung", command=hitung)
hitung_button.pack(pady=10)

hasil_var = tk.StringVar()
hasil_var.set("Total Rp: ")
hasil_label = ttk.Label(window, textvariable=hasil_var)
hasil_label.pack()

window.mainloop()
