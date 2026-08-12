# Contoh penggunaan operator

nilai = 85
tugas = 90
hadir = True

# Operator aritmatika
total = nilai + tugas
rata_rata = total / 2

print("Total nilai:", total)
print("Rata-rata:", rata_rata)

# Lulus jika rata-rata >= 75 DAN hadir
lulus = rata_rata >= 75 and hadir
print("Lulus?", lulus)

# Mendapatkan penghargaan jika nilai >= 90 ATAU tugas >= 90
penghargaan = nilai >= 90 or tugas >= 90
print("Mendapat penghargaan?", penghargaan)

# Tidak lulus jika tidak hadir
tidak_hadir = not hadir
print("Tidak hadir?", tidak_hadir)