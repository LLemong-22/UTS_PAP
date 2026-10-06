import random

TOTAL_LANTAI = 11
HADIAH_GOLD_REGULER = 10
HADIAH_GOLD_BOSS = 911
TOTAL_GOLD_MAKSIMAL = 1011

def buat_nama_monster():
    nama_rand=random.randint(1,6)
    if nama_rand==1:
        nama_anggota="Owen"
    elif nama_rand==2:
        nama_anggota="Christoph"
    elif nama_rand ==3:
        nama_anggota="Lionel"
    elif nama_rand==4:
        nama_anggota="Joel"
    elif nama_rand==5:
        nama_anggota="Evan"
    else:
        nama_anggota="Yosia"

    materi_rand=random.randint(1,6)
    if materi_rand==1:
        nama_materi="Garis singgung"
    elif materi_rand==2:
        nama_materi="Turunan"
    elif materi_rand ==3:
        nama_materi="Integral"
    elif materi_rand==4:
        nama_materi="Limit"
    elif materi_rand==5:
        nama_materi="Asimtot"
    else:
        nama_materi="Diferensial"

    return nama_anggota + " " + nama_materi


def soal_reguler():
    tipe_op = random.randint(1,4)
    a= random.randint(5,20)
    b=random.randint(1,10)

    nama_monster = buat_nama_monster()

    if tipe_op==1:
        teks_soal=f"{a} + {b} = ?"
        jawaban_benar = a+b
    elif tipe_op ==2:
        if a<b:
            a,b=b,a
        teks_soal=f"{a} - {b} = ?"
        jawaban_benar =a-b
    elif tipe_op==3:
        teks_soal= f"{a} * {b} = ?"
        jawaban_benar=a*b
    else:
        hasil_kali=a*b
        teks_soal=f"{hasil_kali} / {b} = ?"
        jawaban_benar = a
    return nama_monster, teks_soal,jawaban_benar,HADIAH_GOLD_REGULER

def soal_boss():
    nama_monster = "SANGAR PhD (Dosen penguji MATH1011)"
    total_putaran=random.randint(20,30)
    dmg_player = random.randint(1500,2500)
    hp_boss=total_putaran*dmg_player
    jawaban_benar = total_putaran   

    teks_soal=(
        f"SANGAR PhD turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss         : {hp_boss:,}\n"
        f"- DMG senjatamu    : {dmg_player:,} / putaran\n\n"    
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk enghabisis HP Boss sampai 0?"
    )
    return nama_monster, jawaban_benar, teks_soal, HADIAH_GOLD_BOSS


def jawaban_salah(jawaban_benar):
    salah1 = jawaban_benar + random.randint(1,4)
    salah2 = jawaban_benar - random.randint(1,4)
    salah3 = jawaban_benar + random.randint(5,8)

    if salah2 <=0:
        salah2=jawaban_benar + random.randint(9,12)

    return salah1,salah2,salah3


def pilihan_jawaban(posisi_benar,benar,s1,s2,s3):
    if posisi_benar==1:
        print(f"A. {benar}")
        print(f"B. {s1}")
        print(f"C. {s2}")
        print(f"D. {s3}")
        return "A"
    if posisi_benar==2:
        print(f"A. {s1}")
        print(f"B. {benar}")
        print(f"C. {s2}")
        print(f"D. {s3}")
        return "B"
    if posisi_benar==3:
        print(f"A. {s2}")
        print(f"B. {s1}")
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
        jawaban!="A" and jawaban!="B" and jawaban!="C" and jawaban!="D"
    ):
        print(">>> pilihan jawaban tidak valid! Harap masukkan hanya A,B,C atau D.")
        jawaban= input(prompt_teks).strip().upper()
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
        pesan2 = "membawa pulang seluruh harta karun dari Tower of MATH1011"
    elif total_gold >= 911:
        kategori = "Penakluk Sangar"
        pesan1 = "Berhasil menaklukkan Final Boss di lantai 11"
        pesan2 = "dan membawa pulang rampasan harta terbesar."
    elif total_gold >= 10:
        kategori = "Kurang Sangar"
        pesan1 = "Berhasil mengumpulkan Gold dari monster biasa,"
        pesan2 = "namun gagal menaklukkan tantangan lantai 11."
    else:
        kategori = "Tidak Sangar"
        pesan1 = "Gagal menjawab seluruh pertanyaan di setiap"
        pesan2 = "lantai menara."

    print(f"Kategori Petualang          : {kategori}")
    print(f"Pesan Petualangan           : {pesan1}")
    print(f"                              {pesan2}")
    print("==================================================")


def main():
    total_gold=0
    print("\n" + "=" * 50)
    print("      SELAMAT DATANG DI TOWER OF MATH1011      ")
    print("  Kumpulkan kepingan Gold dan taklukkan Puncak! ")
    print("=" * 50 + "\n")

    for lantai in range(1,TOTAL_LANTAI+1):
        if lantai<=10:
            nama_monster, teks_soal, jawaban_benar, bobot_gold = (soal_reguler())
            print("==================================================")
            print(
                f"[FLOOR {lantai} / {TOTAL_LANTAI}] | TOTAL GOLD: {total_gold} GOLD"
            )
            print(f"Monster {nama_monster} menghadang jalanmu!")
            print("==================================================")
            print(f"Pertanyaan: Serang titik lemahnya dengan menjawab: {teks_soal}")
        else:
            nama_monster, jawaban_benar, teks_soal, bobot_gold =(soal_boss())
            print("==================================================")
            print(">>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<")
            print(f">>> FINAL BOSS: {nama_monster} <<<")
            print(f"Hadiah Kemenangan: {HADIAH_GOLD_BOSS} GOLD")
            print("==================================================")
            print(teks_soal)

        s1,s2,s3=(jawaban_salah(jawaban_benar))
        posisi = random.randint(1,4)
        kunci = pilihan_jawaban(posisi,jawaban_benar,s1,s2,s3)

        jawaban_user = validasi_jawaban("Jawaban Anda (A/B/C/D): ")

        if jawaban_user == kunci:
            total_gold += HADIAH_GOLD_REGULER
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