# contoh perhitungan metode klasik

import math

# function kombinasi
def kombinasi(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# Menginput data
laki_laki = int(input("Masukkan jumlah siswa laki-laki: "))
perempuan = int(input("Masukkan jumlah siswa perempuan: "))
total_siswa = laki_laki + perempuan
jumlah_laki_laki = int(input("Masukkan jumlah siswa laki-laki yang terpilih: "))
jumlah_perempuan = int(input("Masukkan jumlah siswa perempuan yang terpilih: "))
jumlah_terpilih = jumlah_perempuan + jumlah_laki_laki

# Menghitung n(S)
n_s = kombinasi(total_siswa, jumlah_terpilih)

# Menghitung n(E)
n_e = kombinasi(perempuan, jumlah_perempuan) * kombinasi(laki_laki, jumlah_laki_laki)

# Menghitung peluang P(E)
peluang_pembilang = n_e
peluang_penyebut = n_s

# Sederhanakan pecahan
def sederhanakan_pecahan(pembilang, penyebut):
    faktor_pembagi = math.gcd(int(pembilang), int(penyebut))
    return int(pembilang) // faktor_pembagi, int(penyebut) // faktor_pembagi

peluang_pembilang, peluang_penyebut = sederhanakan_pecahan(peluang_pembilang, peluang_penyebut)

print(f"n(S) = {n_s}")
print(f"n(E) = {n_e}")
print(f"P(E) = {peluang_pembilang}/{peluang_penyebut}")
