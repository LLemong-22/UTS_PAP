import random

TOTAL_LANTAI = 11
HADIAH_GOLD_REGULER = 10
HADIAH_GOLD_BOSS = 911
TOTAL_GOLD_MAKSIMAL = 1011


def buat_nama_monster():
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


def teks_soal_reguler(tipe_op, a, b):
    if tipe_op == 1:
        return f"{a} + {b} = ?"
    elif tipe_op == 2:
        return f"{a} - {b} = ?"
    elif tipe_op == 3:
        return f"{a} * {b} = ?"
    else:
        hasil_kali = a * b
        return f"{hasil_kali} / {b} = ?"


def jawaban_reguler(tipe_op, a, b):
    if tipe_op == 1:
        return a + b
    elif tipe_op == 2:
        return a - b
    elif tipe_op == 3:
        return a * b
    else:
        hasil_kali = a * b
        return hasil_kali // b


def teks_soal_boss(total_putaran, dmg_player):
    hp_boss = total_putaran * dmg_player
    teks_soal = (
        f"SANGAR PhD turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss        : {hp_boss:,}\n"
        f"- DMG Senjatamu  : {dmg_player:,} / putaran\n\n"
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?"
    )
    return teks_soal


def jawaban_salah(jawaban_benar, urutan):
    if urutan == 1:
        return jawaban_benar + random.randint(1, 4)
    elif urutan == 2:
        salah = jawaban_benar - random.randint(1, 4)
        if salah <= 0:
            salah = jawaban_benar + random.randint(9, 12)
        return salah
    else:
        return jawaban_benar + random.randint(5, 8)


def pilihan_jawaban(posisi_benar, benar, s1, s2, s3):
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


def validasi_jawaban(prompt_teks):
    jawaban = input(prompt_teks).strip().upper()
    while (
        jawaban != "A" and jawaban != "B" and jawaban != "C" and jawaban != "D"
    ):
        print(">> Pilihan tidak valid! Harap masukkan hanya A, B, C, atau D.")
        jawaban = input(prompt_teks).strip().upper()
    return jawaban


def hasil_akhir(total_gold):
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


def main():
    total_gold = 0

    print("\n" + "=" * 50)
    print("      SELAMAT DATANG DI TOWER OF MATH1011      ")
    print("  Kumpulkan kepingan Gold dan taklukkan Puncak! ")
    print("=" * 50 + "\n")

    for lantai in range(1, TOTAL_LANTAI + 1):
        if lantai <= 10:
            nama_monster = buat_nama_monster()
            tipe_op = random.randint(1, 4)
            a = random.randint(5, 20)
            b = random.randint(1, 10)

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

        s1 = jawaban_salah(jawaban_benar, 1)
        s2 = jawaban_salah(jawaban_benar, 2)
        s3 = jawaban_salah(jawaban_benar, 3)
        posisi = random.randint(1, 4)
        kunci = pilihan_jawaban(posisi, jawaban_benar, s1, s2, s3)

        jawaban_user = validasi_jawaban("Jawaban Anda (A/B/C/D): ")

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

    print()
    hasil_akhir(total_gold)


main()