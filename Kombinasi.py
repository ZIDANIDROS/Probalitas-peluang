# 2. Aturan Menghitung Untuk Kombinasi

import math

def hitung_kombinasi(n, k):
    kombinasi = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return kombinasi

try:
    n = int(input("Masukkan nilai n: "))
    k = int(input("Masukkan nilai k: "))

    if n < 0 or k < 0 or k > n:
        print("Masukkan angka yang valid (n >= 0, k >= 0, dan k <= n).")
    else:
        hasil_kombinasi = hitung_kombinasi(n, k)
        print(f"Kombinasi dari {n} dan {k} adalah: {hasil_kombinasi}")
except ValueError:
    print("Masukkan angka yang valid.")
