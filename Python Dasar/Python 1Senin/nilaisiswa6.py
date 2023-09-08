x = float(input('Masukkan Nilai Siswa: '))

if x >= 75:
    print("Tuntas")
else:
    mengulang = input("Apakah siswa mengulang [ya/tidak]: ")
    if mengulang.lower() == "ya":
        print("Mengulang")
    else:
        print("Tidak tuntas")
