#Iteratif
def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

print("===PROGRAM ITERATIF===\n")
print("Raka Emillul Fata")
print("NIM : 552010125011\n")
n = int(input("Masukkan nilai n: "))
print("Hasil (Iteratif):", faktorial_iteratif(n))