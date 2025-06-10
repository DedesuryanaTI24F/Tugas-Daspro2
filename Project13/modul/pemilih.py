listPemilih = []

def tambah_pemilih():
    idPemilih = input("Masukan ID Pemilih: ")
    if any(p['id'] == idPemilih for p in listPemilih):
        print("ID sudah terdaftar.")
        return
    namaPemilih = input("Masukan Nama Pemilih: ")
    jurPemilih = input("Masukan Jurusan Pemilih: ")
    
    listPemilih.append({"id": idPemilih, "nama": namaPemilih, "jurusan": jurPemilih, "sudah_memilih": False})
    print("Pemilih berhasil didaftarkan!")

def get_data():
    return listPemilih

def cari_pemilih(id):
    for p in listPemilih:
        if p['id'] == id:
            return p
    return None