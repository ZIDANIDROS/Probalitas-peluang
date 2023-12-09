# menginput data
jumlah_jual = int(input("Masukkan jumlah transaksi jual: "))
jumlah_beli = int(input("Masukkan jumlah transaksi beli: "))
total_transaksi = int(input("Masukkan total jumlah transaksi saham: "))

# Menghitung probabilitas
probabilitas_jual = jumlah_jual / total_transaksi
probabilitas_beli = jumlah_beli / total_transaksi

# Menampilkan hasil dengan format persentase
print("Probabilitas relatif adalah:")
print(f"Jual: {jumlah_jual}/{total_transaksi} = {probabilitas_jual * 100:.2f}%")
print(f"Beli: {jumlah_beli}/{total_transaksi} = {probabilitas_beli * 100:.2f}%")
