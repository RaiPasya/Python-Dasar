def hitung_rata_rata(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return rata_rata

def input_angka():
    angka = []
    while True:
        try:
            bilangan = float(input("Masukan Angka (0 Untuk Mengakhiri): "))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("Masukan Angka Yang Valid.")
    return angka

if __name__ == "__main__":
    print("Program Menghitung Rata-Rata")
    daftar_angka = input_angka()

    if daftar_angka:
        rata_rata = hitung_rata_rata(daftar_angka)
        print(f"Rata-Rata Dari Angka Yang Dimasukan Adalah: {rata_rata:.2f}")
    else:
        print("Tidak Ada Angka Yang Dimasukan")
