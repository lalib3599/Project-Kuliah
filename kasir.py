print('==========TOKO OGAH BANGKRUT==========')
pembeli = input('Masukkan nama pembeli : ')
print(pembeli)
def makanan() :
    global total_makanan
    global porsi
    global makan
    print('\n-------------MENU MAKANAN-------------')
    print('1. Nasi Uduk - Rp.4000,00')
    print('2. Nasi pecel - Rp.5000,00')
    print('3. Nasi Campur - Rp.7000,00')
    nomor = int(input('Masukkan Pilihan 1/2/3 : '))
    porsi = int(input('Berapa porsi : '))
    if nomor == 1:
        total_makanan = porsi * 4000
        print(porsi,'Nasi Uduk - Rp.',total_makanan)
        makan = ('Nasi Uduk')
    elif nomor == 2:
        total_makanan = porsi * 5000
        print(porsi,'Nasi Pecel - Rp.',total_makanan)
        makan = ('Nasi Pecel')
    elif nomor == 3:
        total_makanan = porsi * 7000
        print(porsi,'Nasi Campur - Rp.',total_makanan)
        makan = ('Nasi Campur')
    else :
        print('Pilihan Menu Tidak Tersedia')

def minuman() :
    global total_minuman
    global gelas
    global minum
    print('\n-------------MENU MINUMAN-------------')
    print('1. Es teh manis - Rp.3000,00')
    print('2. Es Jeruk - Rp.4000,00')
    print('3. Es Jus - Rp.5000,00')
    nomor = int(input('Masukkan Pilihan 1/2/3 : '))
    gelas = int(input('Berapa porsi : '))
    if nomor == 1:
        total_minuman = gelas * 3000
        print(gelas,'Es teh manis - Rp.',total_minuman)
        minum = ('Es teh manis')
    elif nomor == 2:
        total_minuman = gelas * 4000
        print(gelas,'Es Jeruk - Rp.',total_minuman)
        minum = ('Es Jeruk')
    elif nomor == 3:
        total_minuman = gelas * 5000
        print(gelas,'Es Jus - Rp.',total_minuman)
        minum = ('Es Jus')
    else :
        print('Pilihan Menu Tidak Tersedia')
makanan()
minuman()
total_semua = total_makanan + total_minuman

print('\nTotal yang harus dibayar : ', total_semua)
uang = int(input('Uang Tunai Pembeli : '))
kembalian = int(uang - total_semua)
print('Kembalian : ',kembalian)

print('===========STRUK PEMBELIAN===========')
print('Nama\t\t:',pembeli)
print('beli\t\t:',porsi,makan,'(Rp.',total_makanan,')')
print('beli\t\t:',gelas,minum,'(Rp.',total_minuman,')')
print('Tagihan\t\t:',total_semua)
print('Dibayar\t\t:',uang)
print('Kembalian\t\t:',kembalian)

print('======================================')
print('======================================')