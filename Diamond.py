# Tentukan 'n' sebagai setengah tinggi wajik (tanpa baris tengah terlebar)
# Untuk pola di gambar dengan total 11 baris, n = 5
n = 5

# BAGIAN ATAS (Segitiga Biasa - 6 baris)
# Perulangan ini mencetak baris 1 sampai 6 (baris tengah terlebar)
for i in range(n + 1):
    # Cetak spasi di kiri (berkurang seiring bertambahnya i)
    # n-i menghasilkan 5, 4, 3, 2, 1, 0 spasi
    print(" " * (n - i), end="")
    # Cetak bintang (bertambah ganjil: 1, 3, 5, 7, 9, 11)
    print("*" * (2 * i + 1))
    
# BAGIAN BAWAH (Segitiga Terbalik - 5 baris)
# Perulangan ini mencetak baris 7 sampai 11, mulai dari baris setelah baris tengah
for i in range(n - 1, -1, -1):
    # Cetak spasi di kiri (bertambah seiring berkurangnya i)
    # n-i menghasilkan 1, 2, 3, 4, 5 spasi
    print(" " * (n - i), end="")
    # Cetak bintang (berkurang ganjil: 9, 7, 5, 3, 1)
    print("*" * (2 * i + 1))