import matplotlib.pyplot as plt

def main():
    # 1. Inisialisasi Array untuk menampung nilai
    nilaiMahasiswa =[]
    totalMahasiswa = 10

    print(f"--- Masukkan {10} Nilai Mahasiswa ---")

    # Input 10 nilai menggunakan perulangan
    for i in range(10):
        while True:
            try:
                nilai = float(input(f"Nilai mahasiswa ke-{i+1}: "))
                if 0 <= nilai <= 100:
                    nilaiMahasiswa.append(nilai)
                    break
                else:
                    print("Error: Masukkan nilai dengan rentang 0 - 100.")
            except ValueError:
                print("Error: Input tidak valid. Harap masukkan angka.")

    # 2. Tampilkan nilai tertinggi & terendah
    nTertinggi = max(nilaiMahasiswa)
    nTerendah = min(nilaiMahasiswa)

    # 3. Hitung rata-rata
    rata_rata = sum(nilaiMahasiswa) / totalMahasiswa

    # 4. Hitung jumlah mahasiswa lulus (>= 60)
    jumlah_lulus = sum(1 for n in nilaiMahasiswa if n >= 60)
    jumlah_gagal = 10 - jumlah_lulus

    # Menampilkan Hasil Teks
    print("\n===============================")
    print("   REKAPITULASI NILAI KELAS    ")
    print("===============================")
    print(f"Seluruh Nilai   : {nilaiMahasiswa}")
    print(f"Nilai Tertinggi : {nTertinggi}")
    print(f"Nilai Terendah  : {nTerendah}")
    print(f"Rata-rata Kelas : {rata_rata:.2f}")
    print(f"Jumlah Lulus    : {jumlah_lulus} Orang (>= 60)")
    print(f"Jumlah Gagal    : {jumlah_gagal} Orang (< 60)")
    print("===============================\n")

    # 5 & 6. Membuat Visualisasi Grafik (Matplotlib)
    plt.figure(figsize=(12, 5)) # Mengatur ukuran kanvas

    # Grafik 1: Bar Chart untuk Nilai Tertinggi dan Terendah
    plt.subplot(1, 2, 1) # (baris, kolom, posisi)
    kategori_ekstrem = ['Nilai Terendah', 'Nilai Tertinggi']
    data_ekstrem = [nTerendah, nTertinggi]
    plt.bar(kategori_ekstrem, data_ekstrem, color=['#e74c3c', '#2ecc71'])
    plt.title('Perbandingan Nilai Terendah & Tertinggi')
    plt.ylabel('Skor Nilai')
    plt.ylim(0, 110)

    # Menambahkan label angka di atas bar
    for i, v in enumerate(data_ekstrem):
        plt.text(i, v + 2, str(v), ha='center', fontweight='bold')

    # Grafik 2: Pie Chart untuk Data Kelulusan
    plt.subplot(1, 2, 2)
    label_kelulusan = ['Lulus (>=60)', 'Tidak Lulus (<60)']
    data_kelulusan = [jumlah_lulus, jumlah_gagal]
    warna =['#3498db', '#f1c40f']

    # Mencegah error jika salah satu data kosong (0)
    if sum(data_kelulusan) > 0:
        plt.pie(data_kelulusan, labels=label_kelulusan, autopct='%1.1f%%', colors=warna, startangle=140, explode=(0.05, 0))
    plt.title('Persentase Data Kelulusan')

    plt.tight_layout()
    plt.show()

# Menjalankan program utama
if __name__ == "__main__":
    main()