# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0
while(True):
    nama_barang = input('Masukan Nama Barang ')
    harga_barang = int(input('Masukan Harga Barang '))
    persen = int(input('Masukan Persentase Laba'))
    barang_terjual = int(input('Masukan Jumlah Barang '))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    #menghitung modal
    modal = harga_barang * barang_terjual
    #modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    #menghitung laba
    laba = keuntungan_persen * barang_terjual
    #laba keseluruhan
    modal_keseluruhan = laba_keseluruhan + modal

    print('barang', nama_barang)
    print('harga barang', harga_barang)
    print('Dijual dengan harga', harga_jual)
    print('terjual', barang_terjual)
    print('modal', modal)
    print('laba', laba)

    apakahLanjut = input('apakah ada tambahan? Y lanjut')
    if(apakahLanjut != 'Y') :
        break
print('===============================================')
print('Modal Keseluruhan', modal_keseluruhan)
print('Laba Keseluruhan', laba_keseluruhan)