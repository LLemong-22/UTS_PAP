import random


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

def main():
    total_gold = 0
    print("\n" + "=" * 50)
    print("      SELAMAT DATANG DI TOWER OF MATH1011       ")
    print("  Kumpulkan kepingan Gold dan taklukkan Puncak! ")
    print("=" * 50 + "\n")

    for lantai in range(1, TOTAL_LANTAI + 1):
        if lantai <= 10:
            nama_monster, teks_soal, jawaban_benar, bobot_gold = generate_soal_reguler()
            print("==================================================")
            print(f"[FLOOR {lantai} / {TOTAL_LANTAI}] | TOTAL GOLD: {total_gold} GOLD")
            print(f"Monster {nama_monster} menghadang jalanmu!")
            print("==================================================")
            print(f"Pertanyaan: Serang titik lemahnya dengan menjawab: {teks_soal}")
        else:
            nama_monster, teks_soal, jawaban_benar, bobot_gold = generate_soal_boss()
            print("==================================================")
            print(">>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<")
            print(f">>> FINAL BOSS: {nama_monster} <<<")
            print(f"Hadiah Kemenangan: {bobot_gold} GOLD")
            print("==================================================")
            print(teks_soal)

        s1, s2, s3 = buat_distraktor(jawaban_benar)
        posisi = random.randint(1, 4)
        kunci = tampilkan_pilihan(posisi, jawaban_benar, s1, s2, s3)

        jawaban_user = validasi_input_jawaban("Jawaban Anda (A/B/C/D): ")

        if jawaban_user == kunci:
            total_gold += bobot_gold
            if lantai == 11:
                print(f"\n>> FATALITY! {nama_monster} DIKALAHKAN, Anda memperoleh +{bobot_gold} Gold!\n")
            else:
                print(f"\n>> CRITICAL HIT! Monster {nama_monster} kalah, Anda memperoleh +{bobot_gold} Gold!\n")
        else:
            if lantai == 11:
                print(f"\n>> YOU DIED! Anda gagal menaklukkan {nama_monster}. Kunci jawaban adalah {kunci} ({jawaban_benar} putaran).\n")
            else:
                print(f"\n>> SERANGAN MELESET! Kunci jawaban yang tepat adalah {kunci}.\n")

    print()
    tampilkan_hasil_ekspedisi(total_gold)