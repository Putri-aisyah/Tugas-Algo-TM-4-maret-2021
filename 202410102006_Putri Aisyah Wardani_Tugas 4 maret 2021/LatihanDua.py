# kalimat = input('Ketikkan kalimat anda: ').lower()
# for i in sorted(set(kalimat)):
#     isi = kalimat.count(i)
#     print(f'huruf {i} berjumlah {isi}')

kalimat = input('Ketikkan kalimat anda: ').lower()
huruf = []
JumlahHuruf = []
abjad = 'abcdefghijklmnopqrstuvwxyz'

for i in kalimat:
    if i not in huruf and i in abjad:
        huruf.append(i)

print(huruf, 'berjumlah', len(huruf))

for i in huruf:
    isi = kalimat.count(i)
    JumlahHuruf.append(isi)

for i in range(len(huruf)):
    print(f'{huruf[i]} berjumlah {JumlahHuruf[i]}')