import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Parkir")
        self.root.geometry("1000x600")

        self.pelanggan = []
        
        self.label_aplikasi_parkir = tk.Label(root, text="Aplikasi Parkir", font=("Arial", 16))
        self.label_aplikasi_parkir.grid(row=0, column=0, columnspan=4, pady=(10, 20))

        self.label_cari_nopol = tk.Label(root, text="Cari NoPol:")
        self.label_cari_nopol.grid(row=1, column=0, sticky="w")
        
        self.entry_cari_nopol = tk.Entry(root)
        self.entry_cari_nopol.grid(row=1, column=1, pady=(0, 10))
        
        self.btn_cari = tk.Button(root, text="Cari", command=self.cari_nopol)
        self.btn_cari.grid(row=1, column=2)
        
        self.label_nopol = tk.Label(root, text="No Plat Polisi:")
        self.label_nopol.grid(row=2, column=0, sticky="w")
        
        self.entry_nopol = tk.Entry(root)
        self.entry_nopol.grid(row=2, column=1, pady=(0, 10))
        
        self.label_waktu_masuk = tk.Label(root, text="Waktu Masuk (HH):")
        self.label_waktu_masuk.grid(row=3, column=0, sticky="w")
        
        self.entry_waktu_masuk = tk.Entry(root)
        self.entry_waktu_masuk.grid(row=3, column=1, pady=(0, 10))
        
        self.label_waktu_keluar = tk.Label(root, text="Waktu Keluar (HH):")
        self.label_waktu_keluar.grid(row=4, column=0, sticky="w")
        
        self.entry_waktu_keluar = tk.Entry(root)
        self.entry_waktu_keluar.grid(row=4, column=1, pady=(0, 10))
        
        self.btn_simpan = tk.Button(root, text="Simpan", command=self.simpan_data)
        self.btn_simpan.grid(row=5, column=0, columnspan=4, pady=(0, 10))

        self.label_biaya_perjam = tk.Label(root, text="Biaya PerJam Rp 2.000", font=("Arial", 14), fg="orange")
        self.label_biaya_perjam.grid(row=6, column=0, columnspan=4, pady=(10, 20))

        self.label_daftar_pelanggan = tk.Label(root, text="Daftar Pelanggan")
        self.label_daftar_pelanggan.grid(row=7, column=0, columnspan=2, pady=(0, 10))

        self.listbox_pelanggan = tk.Listbox(root, font=("Arial", 14), width=40, height=5)
        self.listbox_pelanggan.grid(row=8, column=0, columnspan=2, padx=10)

        self.label_daftar_pelanggan_bayar = tk.Label(root, text="Daftar Pelanggan Bayar")
        self.label_daftar_pelanggan_bayar.grid(row=7, column=2, columnspan=2, pady=(0, 10))

        self.listbox_pelanggan_bayar = tk.Listbox(root, font=("Arial", 14), width=40, height=5)
        self.listbox_pelanggan_bayar.grid(row=8, column=2, columnspan=2, padx=10)
        
    def cari_nopol(self):
        nopol = self.entry_cari_nopol.get()
        found = False
        for data in self.pelanggan:
            if data[0] == nopol:
                found = True
                waktu_masuk, waktu_keluar, biaya = data[1], data[2], data[3]
                messagebox.showinfo("Info", f"NoPol: {nopol}\nJam Masuk: {waktu_masuk}\nJam Keluar: {waktu_keluar}\nBiaya: {biaya}")
                break
        
        if not found:
            messagebox.showinfo("Info", f"NoPol {nopol} tidak ditemukan")
    
    def simpan_data(self):
        nopol = self.entry_nopol.get()
        jam_masuk = self.entry_waktu_masuk.get()
        jam_keluar = self.entry_waktu_keluar.get()
        
        try:
            jam_masuk = int(jam_masuk)
            jam_keluar = int(jam_keluar)
        except ValueError:
            messagebox.showerror("Error", "Format jam salah. Gunakan angka untuk jam (HH).")
            return
        
        if jam_masuk < 0 or jam_masuk > 23 or jam_keluar < 0 or jam_keluar > 23:
            messagebox.showerror("Error", "Jam harus dalam rentang 0 hingga 23.")
            return
        
        biaya = (jam_keluar - jam_masuk) * 2000
        
        self.pelanggan.append([nopol, jam_masuk, jam_keluar, biaya])
        
        self.listbox_pelanggan.insert(tk.END, f"NoPol: {nopol}, Jam Masuk: {jam_masuk}, Jam Keluar: {jam_keluar}, Biaya: {biaya}")
        self.listbox_pelanggan_bayar.insert(tk.END, f"NoPol: {nopol}, Jam Masuk: {jam_masuk}, Jam Keluar: {jam_keluar}, Biaya: {biaya}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()
