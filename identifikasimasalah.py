nama_pemilik_kendaraan = str(input('masukan Nama Pemilik Kendaraan : '))
jenis_kendaraan = str (input('Masukan Jenis Kendaraan Truk/Mobil/Bus/Motor :'))
berat_kendaraan = int (input('Masukan berat Kapasitas Kendaraan dalam Kilogram :'))
nomer_plat = (input('Masukan Nomer Plat Kendaraan :'))
syarat =  berat_kendaraan < 24000 
print (f'Pemilik Kendaraan : {nama_pemilik_kendaraan}')
print (f'Jenis Kendaraan : {jenis_kendaraan}')
print (f'Berat Kendaraan : {berat_kendaraan}')
print (f'Plat nomor: {nomer_plat}')

if syarat : 
    print ('Kendaraan Dapat Menaiki Kapal')
else :
    print ('Berat Kapasitas Kendaraan Terlalu Berat , Kendaraan tidak dapat Menaiki Kapal ')
