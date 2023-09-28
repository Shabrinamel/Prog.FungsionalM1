def hitung_nilai_akhir(uts, uas):
    # Fungsi ini menghitung nilai akhir berdasarkan nilai UTS dan UAS
    return (uts + uas) / 2

def hitung_nilai_akhir_semua(data_mahasiswa):
    # Fungsi ini menghitung nilai akhir semua mahasiswa dalam data_mahasiswa
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai["uts"], nilai["uas"])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    # Fungsi ini menampilkan nilai akhir semua mahasiswa
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        # Data Mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
        "Mahasiswa 1": {"uts": 80, "uas": 85},
        "Mahasiswa 2": {"uts": 75, "uas": 90},
        "Mahasiswa 3": {"uts": 90, "uas": 78},
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
