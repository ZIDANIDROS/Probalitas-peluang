# Menghitung Peluang

def hitung_peluang(kejadian_diinginkan, kejadian_ruang_sampel):
    peluang = kejadian_diinginkan / kejadian_ruang_sampel
    return peluang

try:
    kejadian_diinginkan = int(input("Masukkan jumlah kejadian yang diinginkan: "))
    kejadian_ruang_sampel = int(input("Masukkan jumlah kejadian dalam ruang sampel: "))

    if kejadian_diinginkan < 0 or kejadian_ruang_sampel <= 0:
        print("Masukkan angka yang valid (jumlah kejadian >= 0 dan total kejadian > 0).")
    else:
        hasil_peluang = hitung_peluang(kejadian_diinginkan, kejadian_ruang_sampel)
        print(f"Peluangnya adalah: {hasil_peluang:.2f}")
except ValueError:
    print("Masukkan angka yang valid.")
