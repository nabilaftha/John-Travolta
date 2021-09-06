waktu_kerja = int(input("Masukkan Jam Kerja : "))
gaji = 15000

#fungsi menghitung gaji
if waktu_kerja > 40:
    gaji_pokok = gaji * 40
    waktu_lembur = waktu_kerja - 40
    gaji_lembur = (1.5 * 15000) * waktu_lembur
    total = gaji_pokok + gaji_lembur
else:
    total = gaji * waktu_kerja

pemasukan = int(total)
pengeluaran = int(input("Masukkan Pengeluaran : "))
count = pemasukan - pengeluaran

#fungsi menghitung tabungan
if pemasukan > pengeluaran:
    print('anda bisa menabung sebesar : ' + str(count))
elif pemasukan == pengeluaran:
    print('anda tidak bisa menabung')
else:
    print('cari tambahan sebesar : ' + str(count * -1))