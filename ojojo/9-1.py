def daftar_menu(menu):
    # Menampilkan menu makanan beserta harga
    print("Menu Makanan:")
    for item in menu:
        print("- {} (Rp{})".format(item["nama"], item["harga"]))

# List menu makanan dan harga
menu = [
    {"nama": "Nasi Goreng", "harga": 15000},
    {"nama": "Bakmi nyemek", "harga": 15000},
    {"nama": "Cap Cay", "harga": 13000},
    {"nama": "Kwetiau", "harga": 14000},
    {"nama": "Bakmi Goreng", "harga": 15000},
    {"nama": "Nasi Godok", "harga": 14000},
    {"nama": "Nasi Goreng Magelangan", "harga": 17000},
    {"nama": "Es teh", "harga": 3000},
    {"nama": "Es Jeruk", "harga": 4000},
    {"nama": "Teh Panas", "harga": 3000},
    {"nama": "Jeruk Panas", "harga": 4000},
    {"nama": "Nutrisari", "harga": 4000},
    {"nama": "Kopi", "harga": 5000},
]

# Input dari user
print("Selamat datang di Warkop Berkah!")
daftar_menu(menu)
while True:
    nama_makanan = input("Masukkan makanan yang ingin dipesan: ")
    # Percabangan untuk memastikan makanan yang diminta ada dalam daftar menu
    for item in menu:
        if item["nama"].lower() == nama_makanan.lower():
            print("Harga {}  Rp{}".format(item["nama"], item["harga"]))
            break
    else:
        print("{} tidak ada dalam daftar menu.".format(nama_makanan))
    
    # Input dari user untuk memesan lagi atau tidak
    pesan_lagi = input("Apakah Anda ingin memesan lagi? (y/n): ")
    if pesan_lagi.lower() == "n":
        break

print("Terima kasih atas kunjungan Anda!")
