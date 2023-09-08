x = float(input("Pilih bangun ruang:\n1. Persegi\n2. Persegi Panjang\n3. Trapesium\nPilih: "))

if x == 1:
    s = float(input("\nMasukkan Sisi: "))

    luas = s*s
    keliling = 4*s

    print("Volume Luas:", luas)
    print("Volume Keliling:", keliling)
    
elif x == 2:
    p = float(input("\nMasukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    
    luas = p * l
    keliling = 2*(p+l)
    
    print("Volume Luas:", luas)
    print("Volume Keliling:", keliling)

elif x == 3:
    sa = float(input("\nMasukkan Sisi A: "))
    sb = float(input("Masukkan Sisi B: "))
    sc = float(input("Masukkan Sisi B: "))
    sd = float(input("Masukkan Sisi B: "))
    t = float(input("Masukkan Tinggi: "))
    
    luas = 0.5*(sa + sb)*t
    keliling = sa+sb+sc+sd
    
    print("Volume Luas:", luas)

else:
    print("Pilihan tidak valid")