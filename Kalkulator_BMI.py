berat= int(input("masukkan berat badan anda (kg): "))
tinggi= float(input("masukkan tinggi badan anda (cm): "))

BMI = berat / ((tinggi/100)**2)

if (BMI < 18.5):
    kategori = "kurus (underweight)"
    keterangan = "perlu tambah berat badan"
elif (BMI < 24.9):
    kategori = "normal (ideal)"
    keterangan = "pertahankan gaya hidup sehat"
elif (BMI < 29.9):
    kategori = "gemuk (overweight)"
    keterangan = "perlu olahraga lebih"
else :
    kategori = "obesitas"
    keterangan = "konsultasi ke dokter"
    
    print("NILAI BMI : ", BMI)
    print("kategori : ", kategori)
    print("keterangan : ", keterangan)
