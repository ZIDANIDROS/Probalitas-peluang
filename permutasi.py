# 3. Aturan Menghitung Untuk Kombinasi

import math

def hitung_permutasi(n, k):
    permutasi = math.factorial(n) / math.factorial(n - k)
    return permutasi

try:
    n = int(input("Masukkan nilai n: "))
    k = int(input("Masukkan nilai k: "))

    if n < 0 or k < 0 or k > n:
        print("Masukkan angka yang valid (n >= 0, k >= 0, dan k <= n).")
    else:
        hasil_permutasi = hitung_permutasi(n, k)
        print(f"Permutasi dari {n} dan {k} adalah: {hasil_permutasi}")
except ValueError:
    print("Masukkan angka yang valid.")
