# 1. Aturan Menghitung Untuk Percobaan Multi Langkah

def Multi_Langkah(n1, n2):
    MultiLangkah = n1 * n2
    return MultiLangkah

try:
    n1 = int(input("Masukkan jumlah n1: "))
    n2 = int(input("Masukkan jumlah n2: "))

    if n1 < 0 or n2 <= 0:
        print("Masukkan angka yang valid (1 ~ tak hingga).")
    else:
        hasil_MultiLangkah  = Multi_Langkah(n1, n2)
        print(f"Hasil Multi Langkah nya adalah: {hasil_MultiLangkah}")
except ValueError:
    print("Masukkan angka yang valid.")
