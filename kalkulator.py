def tambah(a, b):
    return a + b
def kurang (a, b):
    return a - b
def kali (a, b):
    return a * b
def bagi (a, b):
    if b == 0:
        return "Error Tidak bisa membagi dengan nol!"
    return a / b

print("=== Kalkulator Sederhana ==")
print("pilih operasi:")
print("1. Tambah")
print("2. kurang")
print("3. kali")
print("4. Bagi")
print("5. Keluar")

while True:
    try:
        pilihan = int(input("\nMasukkan pilihan (1-5): "))
        if pilihan == 5:
            print("Terima kasih sudah pakai kalkulator! Bye, ya! ")
            break
        if pilihan not in [1, 2, 3, 4]:
            print("Pilihan tidak valid! pilih antara 1-5")
            continue
        
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == 1:
            hasil = tambah(angka1, angka2)
            print(f"Hasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == 2:
            hasil = kurang(angka1, angka2)
            print(f"Hasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == 3:
            hasil = kali(angka1, angka2)
            print(f"Hasil: {angka1} * {angka2} = {hasil}")
        elif pilihan == 4:
            hasil = bagi(angka1, angka2)
            print(f"Hasil: {angka1} / {angka2} = {hasil}")

    except ValueError:
        print("Error: Masuk angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")