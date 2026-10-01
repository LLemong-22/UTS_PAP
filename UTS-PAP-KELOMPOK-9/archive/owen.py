import random


def generate_soal_reguler():
    """
    Membangkitkan soal aritmatika dasar (Lantai 1-10) dengan 4 tipe operasi:
    1: Penjumlahan (+), 2: Pengurangan (-), 3: Perkalian (*), 4: Pembagian bulat (//)
    """
    nama_monster = buat_nama_monster()
    tipe_op = random.randint(1, 4)
    a = random.randint(5, 20)
    b = random.randint(1, 10)

    if tipe_op == 1:
        teks_soal = f"{a} + {b} = ?"
        jawaban_benar = a + b
    elif tipe_op == 2:
        if a < b:
            temp = a
            a = b
            b = temp
        teks_soal = f"{a} - {b} = ?"
        jawaban_benar = a - b
    elif tipe_op == 3:
        teks_soal = f"{a} * {b} = ?"
        jawaban_benar = a * b
    else:
        hasil_kali = a * b
        teks_soal = f"{hasil_kali} // {b} = ?"
        jawaban_benar = a

    return nama_monster, teks_soal, jawaban_benar, HADIAH_GOLD_REGULER