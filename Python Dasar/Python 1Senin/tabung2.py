x = float(input("Pilih bangun ruang:\n1. \n2. Balok\nPilihan Anda: "))

if x == 1:
    j = float(input("\nMasukkan jari-jari: "))
    t = float(input("Masukkan tinggi: "))
    
    volume = 3.14 * j * j * t
    
    print("Volume Tabung:", volume)
    
elif x == 2:
    p = float(input("\nMasukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    t = float(input("Masukkan tinggi: "))
    
    volume = p * l * t
    
    print("Volume Balok:", volume)

else:
    print("Pilihan tidak valid")
