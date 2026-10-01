def buat_distraktor(jawaban_benar):
    salah1 = jawaban_benar + random.randint(1, 4)
    salah2 = jawaban_benar - random.randint(1, 4)
    salah3 = jawaban_benar + random.randint(5, 8)

    if salah2 <= 0:
        salah2 = jawaban_benar + random.randint(9, 12)

    return salah1, salah2, salah3

def tampilkan_pilihan(posisi_benar, benar, s1, s2, s3):
    if posisi_benar == 1:
        print(f"A. {benar}\nB. {s1}\nC. {s2}\nD. {s3}")
        return "A"
    elif posisi_benar == 2:
        print(f"A. {s1}\nB. {benar}\nC. {s2}\nD. {s3}")
        return "B"
    elif posisi_benar == 3:
        print(f"A. {s1}\nB. {s2}\nC. {benar}\nD. {s3}")
        return "C"
    else:
        print(f"A. {s1}\nB. {s2}\nC. {s3}\nD. {benar}")
        return "D"