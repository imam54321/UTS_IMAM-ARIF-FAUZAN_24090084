#tahun kabisat
tahun=int(input('Masukan Tahun : '))
tahun_kabisat=tahun % 400
bukan_tahun_kabisat=tahun % 4 and tahun % 100

if tahun == tahun_kabisat:
    nama_tahun='kabisat'
else:
    nama_tahun='bukan kabisat'


print(f'ini adalah {nama_tahun}')

