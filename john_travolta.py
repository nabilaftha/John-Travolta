waktu_kerja = int(input("Masukkan Jam Kerja : "))
gaji = 15000 * 40
waktu_lembur = waktu_kerja - 40
gaji_lembur = 1.5 * 15000 * waktu_lembur
total = gaji + gaji_lembur

pemasukan = int(total)
pengeluaran = 600000

count = pemasukan - pengeluaran

if pemasukan > pengeluaran:
    print('anda bisa menabung sebesar : ' + str(count))
# Ketika kedua variable memiliki nilai yang sama, cetak 'Anda dapat membeli apel tetapi dompet Anda akan menjadi kosong'
elif pemasukan == pengeluaran:
    print('anda tidak bisa menabung')

else:
    print('cari tambahan sebesar : ' + str(count * -1))