data = {
    'nama':'maju jaya',
    'no_nota': '01',
    'kepada' : 'bambang',
    'barang' : [
        (1, 'Penghapus', 1000, 3, 3000), #no,nama,harga satuan,jumlah beli, subtotal
        (2, 'Penggaris', 2000, 10, 20000),
        
    ]
}
for key, value in data.items(): #menghasilkan semua key dan value dalam dictionary
    print(f'{key}:{value}')