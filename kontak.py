# a) Data awal: minimal 3 kontak (nama -> nomor HP)
buku_kontak = {
    "Budi": "081234567890",
    "Siti": "085678901234",
    "Andi": "087890123456"
}

# c) Gunakan while loop untuk menu berulang
while True:
    print("\n=== MENU BUKU KONTAK ===")
    print("1. Lihat Semua Kontak")
    print("2. Cari Kontak (by Nama)")
    print("3. Tambah Kontak Baru")
    print("4. Hapus Kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        # Lihat semua kontak
        print("\n--- DAFTAR KONTAK ---")
        if not buku_kontak:
            print("Buku kontak masih kosong.")
        else:
            for nama, nomor in buku_kontak.items():
                print(f"- {nama}: {nomor}")

    elif pilihan == "2":
        # Cari kontak menggunakan .get() sesuai ketentuan d)
        nama_cari = input("Masukkan nama yang dicari: ")
        nomor = buku_kontak.get(nama_cari)
        
        if nomor:
            print(f"Nomor HP {nama_cari}: {nomor}")
        else:
            print(f"Kontak dengan nama '{nama_cari}' tidak ditemukan.")

    elif pilihan == "3":
        # Tambah kontak baru
        nama_baru = input("Masukkan nama kontak baru: ")
        nomor_baru = input("Masukkan nomor HP: ")
        buku_kontak[nama_baru] = nomor_baru
        print(f"Kontak '{nama_baru}' berhasil ditambahkan!")

    elif pilihan == "4":
        # Hapus kontak
        nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ")
        if nama_hapus in buku_kontak:
            del buku_kontak[nama_hapus]
            print(f"Kontak '{nama_hapus}' berhasil dihapus.")
        else:
            print(f"Kontak dengan nama '{nama_hapus}' tidak ditemukan.")

    elif pilihan == "5":
        # Keluar dari program
        print("Meninggalkan program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")