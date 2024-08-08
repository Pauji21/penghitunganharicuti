from datetime import datetime, timedelta

def cek_cuti_pribadi(tanggal_join, tanggal_cuti, durasi_cuti, cuti_bersama):
    # Konstanta
    CUTI_KANTOR = 14
    CUTI_MAX_BERTURUTAN = 3
    
    # Konversi input ke format datetime
    tanggal_join = datetime.strptime(tanggal_join, "%d-%m-%Y")
    tanggal_cuti = datetime.strptime(tanggal_cuti, "%d-%m-%Y")
    
    # Hitung tanggal mulai cuti pribadi (180 hari setelah tanggal join)
    tanggal_mulai_cuti_pribadi = tanggal_join + timedelta(days=180)
    
    # Jika tanggal rencana cuti sebelum tanggal mulai cuti pribadi
    if tanggal_cuti < tanggal_mulai_cuti_pribadi:
        return (False, "Karyawan belum memenuhi syarat untuk cuti pribadi.")
    
    # Hitung total hari dari tanggal mulai cuti pribadi hingga akhir tahun
    akhir_tahun = datetime(tanggal_cuti.year, 12, 31)
    if tanggal_cuti > akhir_tahun:
        return (False, "Tanggal cuti berada di luar tahun ini.")
    
    total_hari_cuti_pribadi = (akhir_tahun - tanggal_mulai_cuti_pribadi).days + 1
    kuota_cuti_pribadi = (total_hari_cuti_pribadi // 365) * cuti_bersama
    
    # Validasi durasi cuti pribadi
    if durasi_cuti > CUTI_MAX_BERTURUTAN:
        return (False, "Durasi cuti pribadi tidak boleh lebih dari 3 hari berturut-turut.")
    
    # Validasi durasi cuti terhadap kuota yang tersedia
    if durasi_cuti > kuota_cuti_pribadi:
        return (False, "Durasi cuti pribadi melebihi kuota yang tersedia.")
    
    return (True, "Cuti pribadi dapat diambil.")

# Contoh penggunaan
tanggal_join = "01-05-2024"
tanggal_cuti = "01-11-2024"
durasi_cuti = 2
cuti_bersama = 7

hasil, alasan = cek_cuti_pribadi(tanggal_join, tanggal_cuti, durasi_cuti, cuti_bersama)
print(hasil)  # True atau False
print(alasan)  # Alasan dari keputusan
