import random

angka = random.randint(1, 10)
Max_Tebakan = 3
No_Tebakan = 0
Tebakan_true = False

print('Program ini akan memilih angka secara acak dari 1 sampai 10')
print('Anda harus menebak dalam {} percobaan'.format(Max_Tebakan))

petunjuk = 'Ini adalah tebakan ke {} anda. Masukkan angka lalu tekan enter \n'
while not Tebakan_true and not No_Tebakan >= Max_Tebakan:
    No_Tebakan = No_Tebakan + 1
    Tebakan = input(petunjuk.format(No_Tebakan))
    Tebakan = int(Tebakan)
    if Tebakan == angka:
        Tebakan_true = True
    elif Tebakan > angka:
        print('Angka yang anda masukkan terlalu besar')
    else:
        print('Angka yang anda masukkan terlalu kecil')
if Tebakan_true:
    print('Selamat anda berhasil menebak')
else:
    print('GAME OVER!!!')
    print('Jawabannya adalah ',angka)