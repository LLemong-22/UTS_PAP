import random

# ==============================================================================
# KONFIGURASI GLOBAL SISTEM (TOWER OF MATH1011)
# ==============================================================================
TOTAL_LANTAI = 11
HADIAH_GOLD_REGULER = 10
HADIAH_GOLD_BOSS = 911
TOTAL_GOLD_MAKSIMAL = 1011


# ==============================================================================
# TASK 1: GENERATOR SOAL ARITMATIKA DASAR (LANTAI 1-10)
# ==============================================================================
def teks_soal_reguler(tipe_op, a, b):
    """Menyusun teks soal aritmatika dasar (Lantai 1-10) dari 4 tipe operasi:

    1: Penjumlahan (+)
    2: Pengurangan (-)
    3: Perkalian (*)
    4: Pembagian bulat (/) dengan hasil yang selalu pas (tanpa sisa)
    Nilai tipe_op, a, dan b dibangkitkan di main() agar teks soal dan
    jawaban selalu memakai angka yang sama.
    Mengembalikan: teks_soal (string)
    """
    if tipe_op == 1:
        return f"{a} + {b} = ?"
    elif tipe_op == 2:
        return f"{a} - {b} = ?"
    elif tipe_op == 3:
        return f"{a} * {b} = ?"
    else:
        # Menjamin pembagian bilangan bulat yang tepat dan rapi
        hasil_kali = a * b
        return f"{hasil_kali} / {b} = ?"


def jawaban_reguler(tipe_op, a, b):
    """Menghitung jawaban benar untuk soal reguler dengan tipe_op, a, dan b

    yang sama seperti pada teks_soal_reguler().
    Mengembalikan: jawaban_benar (int)
    """
    if tipe_op == 1:
        return a + b
    elif tipe_op == 2:
        return a - b
    elif tipe_op == 3:
        return a * b
    else:
        # Soal berbentuk (a * b) // b, sehingga hasil pembagian bulatnya pasti a
        hasil_kali = a * b
        return hasil_kali // b


# ==============================================================================
# TASK 2: FUNGSI VALIDASI INPUT & HANDLING SANITASI STRING
# ==============================================================================
def validasi_jawaban(prompt_teks):
    """Menerima input dari pengguna, melakukan sanitasi string (strip dan
    upper),

    serta memastikan jawaban hanya berupa salah satu dari huruf 'A', 'B', 'C',
    atau 'D'.
    Murni menggunakan percabangan boolean tanpa struktur koleksi
    list/dict/set/tuple.
    """
    jawaban = input(prompt_teks).strip().upper()
    while (
        jawaban != "A" and jawaban != "B" and jawaban != "C" and jawaban != "D"
    ):
        print(">> Pilihan tidak valid! Harap masukkan hanya A, B, C, atau D.")
        jawaban = input(prompt_teks).strip().upper()
    return jawaban


# ==============================================================================
# TASK 3: ALGORITMA DISTRAKTOR & PENGACAKAN POSISI OPSI (A/B/C/D)
# ==============================================================================
def jawaban_salah(jawaban_benar, urutan):
    """Membangkitkan 1 nilai distraktor (jawaban salah) sesuai urutan (1-3).

    Dipanggil 3 kali dari main(). Rentang tiap urutan tidak saling tumpang
    tindih, sehingga ketiga distraktor dijamin berbeda satu sama lain serta
    berbeda dari jawaban asli. Murni menggunakan kalkulasi skalar dan random.
    Mengembalikan: nilai distraktor (int)
    """
    if urutan == 1:
        return jawaban_benar + random.randint(1, 4)
    elif urutan == 2:
        salah = jawaban_benar - random.randint(1, 4)
        # Antisipasi nilai non-positif untuk soal matematika dasar
        if salah <= 0:
            salah = jawaban_benar + random.randint(9, 12)
        return salah
    else:
        return jawaban_benar + random.randint(5, 8)


def pilihan_jawaban(posisi_benar, benar, s1, s2, s3):
    """Mencetak 4 opsi pilihan ganda (A, B, C, D) berdasarkan posisi kunci (1-4)

    menggunakan percabangan if-elif-else tanpa tipe data list/tuple/dict.
    Mengembalikan huruf kunci jawaban yang benar ('A', 'B', 'C', atau 'D').
    """
    if posisi_benar == 1:
        print(f"A. {benar}")
        print(f"B. {s1}")
        print(f"C. {s2}")
        print(f"D. {s3}")
        return "A"
    elif posisi_benar == 2:
        print(f"A. {s1}")
        print(f"B. {benar}")
        print(f"C. {s2}")
        print(f"D. {s3}")
        return "B"
    elif posisi_benar == 3:
        print(f"A. {s1}")
        print(f"B. {s2}")
        print(f"C. {benar}")
        print(f"D. {s3}")
        return "C"
    else:
        print(f"A. {s1}")
        print(f"B. {s2}")
        print(f"C. {s3}")
        print(f"D. {benar}")
        return "D"


# ==============================================================================
# TASK 4: GENERATOR FINAL BOSS & SIMULASI TEMPUR RPG (LANTAI 11)
# ==============================================================================
def teks_soal_boss(total_putaran, dmg_player):
    """Menyusun teks soal Final Boss (Lantai 11):

    Dosen Penguji MATH1011 'SANGAR PhD' dengan kalkulasi putaran tempur (turns)
    sederhana: membagi total HP Boss dengan DMG senjata per putaran.
    HP Boss dibentuk dari total_putaran * dmg_player sehingga jawabannya
    (total_putaran) selalu bilangan bulat.
    Mengembalikan: teks_soal (string)
    """
    hp_boss = total_putaran * dmg_player

    teks_soal = (
        f"SANGAR PhD turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss        : {hp_boss:,}\n"
        f"- DMG Senjatamu  : {dmg_player:,} / putaran\n\n"
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?"
    )

    return teks_soal


# ==============================================================================
# TASK 5: MODUL REKAPITULASI AKHIR & EVALUASI MATRIKS GOLD
# ==============================================================================
def hasil_akhir(total_gold):
    """Menampilkan layar rekapitulasi skor akhir dan kategori petualang."""
    print("==================================================")
    print("              HASIL EKSPEDISI TOWER               ")
    print("==================================================")
    print(
        f"Total Gold yang Dikumpulkan : {total_gold} / {TOTAL_GOLD_MAKSIMAL} Gold"
    )

    if total_gold == 1011:
        kategori = "Penakluk Super Sangar"
        pesan1 = "Ekspedisi selesai! Anda berhasil"
        pesan2 = "membawa pulang seluruh harta karun"
        pesan3 = "dari Tower of MATH1011!"
    elif total_gold >= 911:
        kategori = "Penakluk Sangar"
        pesan1 = "Berhasil menaklukkan Final Boss di lantai 11"
        pesan2 = "dan membawa pulang rampasan harta terbesar."
        pesan3 = ""
    elif total_gold >= 10:
        kategori = "Kurang Sangar"
        pesan1 = "Berhasil mengumpulkan Gold dari monster biasa,"
        pesan2 = "namun gagal menaklukkan tantangan lantai 11."
        pesan3 = ""
    else:
        kategori = "Tidak Sangar"
        pesan1 = "Gagal menjawab seluruh pertanyaan di setiap"
        pesan2 = "lantai menara."
        pesan3 = ""

    print(f"Kategori Petualang          : {kategori}")
    print(f"Pesan Petualangan           : {pesan1}")
    if pesan2 != "":
        print(f"                              {pesan2}")
    if pesan3 != "":
        print(f"                              {pesan3}")
    print("==================================================")


# ==============================================================================
# TASK 6: GENERATOR NAMA MONSTER & CONTROLLER LOOP UTAMA GAME
# ==============================================================================
def buat_nama_monster():
    """Membangkitkan nama monster unik gabungan nama anggota tim dan istilah

    kalkulus/matematika tanpa tipe data list sesuai silabus Week 1-7.
    """
    rand_nama = random.randint(1, 6)
    if rand_nama == 1:
        nama_anggota = "Owen"
    elif rand_nama == 2:
        nama_anggota = "Christoph"
    elif rand_nama == 3:
        nama_anggota = "Lionel"
    elif rand_nama == 4:
        nama_anggota = "Joel"
    elif rand_nama == 5:
        nama_anggota = "Evan"
    else:
        nama_anggota = "Yosia"

    rand_materi = random.randint(1, 6)
    if rand_materi == 1:
        istilah_mtk = "Garis Singgung"
    elif rand_materi == 2:
        istilah_mtk = "Integral"
    elif rand_materi == 3:
        istilah_mtk = "Turunan"
    elif rand_materi == 4:
        istilah_mtk = "Limit"
    elif rand_materi == 5:
        istilah_mtk = "Asimtot"
    else:
        istilah_mtk = "Diferensial"

    return nama_anggota + " " + istilah_mtk


def main():
    """Fungsi utama game loop: Mengelola alur ekspedisi lantai 1-11,"""
    total_gold = 0

    print("\n" + "=" * 50)
    print("      SELAMAT DATANG DI TOWER OF MATH1011      ")
    print("  Kumpulkan kepingan Gold dan taklukkan Puncak! ")
    print("=" * 50 + "\n")

    for lantai in range(1, TOTAL_LANTAI + 1):
        if lantai <= 10:
            # Lantai Reguler (Lantai 1 - 10)
            nama_monster = buat_nama_monster()
            tipe_op = random.randint(1, 4)
            a = random.randint(5, 20)
            b = random.randint(1, 10)

            # Memastikan hasil pengurangan selalu positif
            if tipe_op == 2 and a < b:
                temp = a
                a = b
                b = temp

            teks_soal = teks_soal_reguler(tipe_op, a, b)
            jawaban_benar = jawaban_reguler(tipe_op, a, b)
            bobot_gold = HADIAH_GOLD_REGULER

            print("==================================================")
            print(
                f"[FLOOR {lantai} / {TOTAL_LANTAI}] | TOTAL GOLD: {total_gold} GOLD"
            )
            print(f"Monster {nama_monster} menghadang jalanmu!")
            print("==================================================")
            print(f"Pertanyaan: Serang titik lemahnya dengan menjawab: {teks_soal}")
        else:
            # Lantai 11: Final Boss
            nama_monster = "SANGAR PhD (Dosen Penguji MATH1011)"
            total_putaran = random.randint(20, 50)
            dmg_player = random.randint(1500, 2500)

            teks_soal = teks_soal_boss(total_putaran, dmg_player)
            jawaban_benar = total_putaran
            bobot_gold = HADIAH_GOLD_BOSS

            print("==================================================")
            print(">>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<")
            print(f">>> FINAL BOSS: {nama_monster} <<<")
            print(f"Hadiah Kemenangan: {bobot_gold} GOLD")
            print("==================================================")
            print(teks_soal)

        # Bangkitkan opsi pilihan ganda
        s1 = jawaban_salah(jawaban_benar, 1)
        s2 = jawaban_salah(jawaban_benar, 2)
        s3 = jawaban_salah(jawaban_benar, 3)
        posisi = random.randint(1, 4)
        kunci = pilihan_jawaban(posisi, jawaban_benar, s1, s2, s3)

        # Validasi input
        jawaban_user = validasi_jawaban("Jawaban Anda (A/B/C/D): ")

        # Evaluasi Jawaban
        if jawaban_user == kunci:
            total_gold += bobot_gold
            if lantai == 11:
                print(
                    f"\n>> FATALITY! {nama_monster} DIKALAHKAN, Anda memperoleh +{bobot_gold} Gold!\n"
                )
            else:
                print(
                    f"\n>> CRITICAL HIT! Monster {nama_monster} kalah, Anda memperoleh +{bobot_gold} Gold!\n"
                )
        else:
            if lantai == 11:
                print(
                    f"\n>> YOU DIED! Anda gagal menaklukkan {nama_monster}. Kunci jawaban adalah {kunci} ({jawaban_benar} putaran).\n"
                )
            else:
                print(
                    f"\n>> SERANGAN MELESET! Kunci jawaban yang tepat adalah {kunci}.\n"
                )

    # Rekapitulasi Akhir
    print()
    hasil_akhir(total_gold)


main()