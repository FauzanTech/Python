# Merupakan tugas akhir dari mata kuliah Aljabar Linear
# Program yang saya buat dengan berpacu pada salah satu sub bab mata kuliah Aljabar Linear
# Program ini saya buat untuk mengubah/enkripsi sebuah kalimat ke dalam bentuk kode
# Program ini hanya mampu memproses matriks berdimensi 2

# Kode import
import numpy as np
from enum import Enum

# Variable 
matrixDefault = []
result = []
batasAwal = 0
batasAkhir = 2

# Perulangan
print("Masukkan matriks 2D: ")
print("""Format: 
<angka1> <angka2>
<angka3> <angka4>""")

for _ in range(2):
    temp = input().split()
    sub = [int(temp[0]), int(temp[1])]
    matrixDefault.append(sub)

# Membuat Matriks
matrixDefault = np.array(matrixDefault)

# Kode untuk meminta kalimat yang akan diubah
kalimat = input("Masukkan kalimat yang ingin diubah: ").upper().replace(" ","")
lenKalimat = len(kalimat)

# Melakukan proses enkripsi
if(not(lenKalimat % 2 == 0)):
    kalimat = list(kalimat)
    kalimat.append(kalimat[-1])


while batasAkhir <= lenKalimat+1:
    new = kalimat[batasAwal:batasAkhir]
    newMatrix = np.array([[ord(new[0])-64],[ord(new[1])-64]])

    newMatrix = matrixDefault.dot(newMatrix)
    newMatrix = list(newMatrix)
    for i in range(len(newMatrix)):
        value = newMatrix[i]%26
        if value == 0:
            result.append('Z')
        else:
            result.append(chr(value[0]+64))
    batasAwal += 2
    batasAkhir += 2

# Menampilkan hasil enksripsi
print("".join(result))
