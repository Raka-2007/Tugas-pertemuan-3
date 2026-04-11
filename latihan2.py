def jumlah_rekursif(n):
    if n == 1:
        return 1
    else:
        return n + jumlah_rekursif(n - 1)
    
n = int(input("Masukkan nilai n: "))
print("Jumlah:", jumlah_rekursif(n))