tinggi_piramida = int(input('Masukan Jumlah Baris: '))
print()

for i in range(tinggi_piramida):
  for j in range(tinggi_piramida-i):
    print(' ',end='')
    
  for k in range(i+1):
    print('* ',end='')
  print()