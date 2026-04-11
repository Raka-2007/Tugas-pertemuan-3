#Raka Emillul Fata
#Latihan 1

import os
#Rekursif

def faktorial_rekursif(n):
    if n == 0:
        return 1
    else:
        #n dikali hasil dari n-1
        #contoh faktorial_rekursif 3 = 3 * faktorial rekursif(2)
        return n * faktorial_rekursif(n - 1)

print("===PROGRAM REKURSIF===\n")
print("Raka Emillul Fata\n")
print("NIM : 552010125011\n")
n = int(input("Masukkan nilai n: "))
print("Hasil (Rekursif):", faktorial_rekursif(n))