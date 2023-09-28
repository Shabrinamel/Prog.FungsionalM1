random_list = [105, 3.1, "Hello", 737, "Python", 27, "World", 412, 5.5, "AI"]

# Inisialisasi struktur data yang akan digunakan
int_dict = {}
float_tuple = ()
string_list = []

# Iterasi melalui elemen-elemen dalam random_list
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
    elif isinstance(item, float):
        # Menyimpan data float dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menyimpan data string dalam list
        string_list.append(item)

# Menampilkan hasil
print("Data integer dalam bentuk dictionary:", int_dict)
print("Data float dalam bentuk tuple:", float_tuple)
print("Data string dalam bentuk list:", string_list)
