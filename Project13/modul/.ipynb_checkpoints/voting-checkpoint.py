from modul import pemilih, calon
def lakukan_voting():
    idPemilih = input("Masukan ID Pemilih: ")
    dataPemilih = pemilih.cari_pemilih(idPemilih)
    if not dataPemilih:
        print("ID Pemilih TIdak Ditemukan!")
        return
        
    if dataPemilih['sudah_memilih']:
        print("ID Sudah Memilih!")
        return
    idCalon = input("Masukan ID Calon: ")
    dataCalon = calon.cari_calon(idCalon)
    if not dataCal:
        print("ID Calon Tidak Ditemukan!")
    dataCalon['jumlah_suara'] += 1
    dataPemilih['sudah_memilih'] = True
    print("Voting Berhasil Dilakukan!")

def tampilkan_hasil():
    print("Hasil Sementara:")
    for c in calon.get_data():
        print(f"{c['nama']} ({c['id']}) - {c['jumlah_suara']} suara")