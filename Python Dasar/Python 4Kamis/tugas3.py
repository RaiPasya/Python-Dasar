import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("500x600")
window.resizable(False, False)
window.title("Data Siswa")

title_label = tk.Label(window, text="DATA SISWA", font=("Arial", 20, "bold"), fg="black", bg="lightblue")
title_label.pack(pady=20)

#data akan muncul di terminal VSC

nama_lengkap = tk.StringVar()
tanggal_lahir = tk.StringVar()
nisn = tk.StringVar()
asal_sk = tk.StringVar()
nama_ayah = tk.StringVar()
nama_ibu = tk.StringVar()
nomor_tlp = tk.StringVar()

def tombol_click():
    nama = nama_lengkap.get()
    tanggal = tanggal_lahir.get()
    nisn_val = nisn.get()
    asal = asal_sk.get()
    namaa = nama_ayah.get()
    namai = nama_ibu.get()
    nomor = nomor_tlp.get()
    print("Nama Lengkap: ", nama)
    print("Tanggal Lahir: ", tanggal)
    print("NISN: ", nisn_val)
    print("Asal Sekolah: ", asal)
    print("Nama Ayah: ", namaa)
    print("Nama Ibu: ", namai)
    print("Nomor Telepon: ", nomor)

def hapus_input():
    nama_lengkap.set("")
    tanggal_lahir.set("")
    nisn.set("")
    asal_sk.set("")
    nama_ayah.set("")
    nama_ibu.set("")
    nomor_tlp.set("")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, fill="x", expand=True)

nama_lengkap_label = ttk.Label(input_frame, text="Nama Lengkap: ")
nama_lengkap_label.pack(padx=10, fill="x", expand=True)

nama_lengkap_entry = ttk.Entry(input_frame, textvariable=nama_lengkap)
nama_lengkap_entry.pack(padx=10, fill="x", expand=True)

tanggal_lahir_label = ttk.Label(input_frame, text="Tanggal Lahir: ")
tanggal_lahir_label.pack(padx=10, fill="x", expand=True)

tanggal_lahir_entry = ttk.Entry(input_frame, textvariable=tanggal_lahir)
tanggal_lahir_entry.pack(padx=10, fill="x", expand=True)

nisn_label = ttk.Label(input_frame, text="NISN: ")
nisn_label.pack(padx=10, fill="x", expand=True)

nisn_entry = ttk.Entry(input_frame, textvariable=nisn)
nisn_entry.pack(padx=10, fill="x", expand=True)

asal_sk_label = ttk.Label(input_frame, text="Asal Sekolah: ")
asal_sk_label.pack(padx=10, fill="x", expand=True)

asal_sk_entry = ttk.Entry(input_frame, textvariable=asal_sk)
asal_sk_entry.pack(padx=10, fill="x", expand=True)

nama_ayah_label = ttk.Label(input_frame, text="Nama Ayah: ")
nama_ayah_label.pack(padx=10, fill="x", expand=True)

nama_ayah_entry = ttk.Entry(input_frame, textvariable=nama_ayah)
nama_ayah_entry.pack(padx=10, fill="x", expand=True)

nama_ibu_label = ttk.Label(input_frame, text="Nama Ibu: ")
nama_ibu_label.pack(padx=10, fill="x", expand=True)

nama_ibu_entry = ttk.Entry(input_frame, textvariable=nama_ibu)
nama_ibu_entry.pack(padx=10, fill="x", expand=True)

nomor_tlp_label = ttk.Label(input_frame, text="Nomor Telepon/ HP: ")
nomor_tlp_label.pack(padx=10, fill="x", expand=True)

nomor_tlp_entry = ttk.Entry(input_frame, textvariable=nomor_tlp)
nomor_tlp_entry.pack(padx=10, fill="x", expand=True)

tombol_simpan = ttk.Button(input_frame, text="Simpan", command=tombol_click)
tombol_simpan.pack(fill="x", expand=True, padx=10, pady=10)

tombol_hapus = ttk.Button(input_frame, text="Hapus", command=hapus_input)
tombol_hapus.pack(fill="x", expand=True, padx=10, pady=10)

window.mainloop()
