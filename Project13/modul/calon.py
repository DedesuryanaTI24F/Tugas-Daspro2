listCalon = []

def tambah_calon():
    idCalon = input("Masukkan ID Calon :")
    if any(c['id'] == idCalon for c in listCalon):
        print("ID sudah terdaftar.")
        return
    namaCalon = input("Masukkan nama Calon :")
    visimisiCalon = input("Masukkan Visi Misi Calon :")

    listCalon.append({"id": idCalon,"Nama": namaCalon, "Visi": visimisiCalon, "Jumlah_suara": 0})
    print("Calon berhasil didaftarkan:")

def get_data():
    return listCalon

def cari_pemilih(id):
    for c in listCalon:
        if c['id'] == id:
            return c
        return None
    
    listCalon = []

