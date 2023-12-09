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









# print(lenKalimat)
# print(len(result))
# dimensiMatrix = int(input("Masukkan dimensi matriks: "))
    # for _ in range(2):
    #     sub.append(int(input()))
# print(matrixDefault)
# print(kalimat)
# print(new)
# print(newMatrix)
# print(list(newMatrix))
# print(value)
# print(matrixDefault)
# print(ord('A')-64)
# print(ord('B')-64)
# print(ord('C')-64)
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[4,5,6],[7,8,9],[1,2,3]])

# print(a)
# print(b)

# print(a.shape)
# print(b.shape)


# print(Abjad)
# class Abjad(Enum):
#     A = 1
#     B = 2
#     C = 3
#     D = 4
#     E = 5
#     F = 6
#     G = 7
#     H = 8
#     I = 9
#     J = 10
#     K = 11
#     L = 12
#     M = 13
#     N = 14
#     O = 15
#     P = 16
#     Q = 17
#     R = 18
#     S = 19
#     T = 20
#     U = 21
#     V = 22
#     W = 23
#     X = 24
#     Y = 25
#     Z = 26


# Abjad = Enum('Abjad', ['A','B','C'])