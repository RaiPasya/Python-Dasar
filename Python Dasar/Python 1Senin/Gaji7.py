n = input('Nama Anda: ')
gaji = float(input('Gaji Anda: '))

tun = 0.20 * gaji
pa = 0.15 * (gaji+tun)
gab = gaji + tun - pa

print("Nama Anda :", n)
print("Gaji Anda :", gaji)
print("Gaji Bersih Anda :", gab)