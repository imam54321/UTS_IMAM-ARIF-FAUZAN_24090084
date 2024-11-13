jumlah_barang=int(input('Masukan Jumlah Barang: '))
Masukan_harga_barang=float

total_barang=0
for a in range(jumlah_barang): 
   harga = float(input(f'Masukan harga barang ke-{a + 1 }:Rp .' ))
   total_barang += harga
   
total_harga= total_barang + total_barang
print(f'total harganya adalah :Rp{total_harga}')