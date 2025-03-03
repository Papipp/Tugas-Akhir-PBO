class Penyewa:
    def __init__(self, nama, kontak):
        self.nama = nama
        self.kontak = kontak

    def __str__(self):
        return f"Penyewa: {self.nama}, Kontak: {self.kontak}"


class Unit:
    def __init__(self, nomor_unit, harga_sewa):
        self.nomor_unit = nomor_unit
        self.harga_sewa = harga_sewa
        self.penyewa = None  # Awalnya unit kosong

    def sewa_unit(self, penyewa):
        if self.penyewa is None:
            self.penyewa = penyewa
            return f"Unit {self.nomor_unit} berhasil disewa oleh {penyewa.nama}"
        return f"Unit {self.nomor_unit} sudah ditempati oleh {self.penyewa.nama}"

    def kosongkan_unit(self):
        if self.penyewa is not None:
            penyewa_keluar = self.penyewa.nama
            self.penyewa = None
            return f"Unit {self.nomor_unit} sekarang kosong. Penyewa sebelumnya: {penyewa_keluar}"
        return f"Unit {self.nomor_unit} sudah kosong"

    def __str__(self):
        status = f"Disewa oleh {self.penyewa.nama}" if self.penyewa else "Kosong"
        return f"Unit {self.nomor_unit}: {status}, Harga Sewa: {self.harga_sewa}"


class Apartemen:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.unit_list = []

    def tambah_unit(self, unit):
        self.unit_list.append(unit)

    def tampilkan_info(self):
        print(f"Apartemen: {self.nama}, Alamat: {self.alamat}")
        for unit in self.unit_list:
            print(unit)

# Contoh Penggunaan
apartemen = Apartemen("Green Residence", "Jl. Merdeka No. 45")
unit1 = Unit("A-101", 5000000)
unit2 = Unit("A-102", 4500000)

apartemen.tambah_unit(unit1)
apartemen.tambah_unit(unit2)

penyewa1 = Penyewa("Budi Santoso", "08123456789")

print(unit1.sewa_unit(penyewa1))  # Menyewa unit A-101
print(unit1.sewa_unit(penyewa1))  # Coba sewa lagi (sudah ditempati)
print(unit1.kosongkan_unit())  # Mengosongkan unit
print(unit1.sewa_unit(penyewa1))  # Menyewa ulang

apartemen.tampilkan_info()  # Menampilkan semua unit
