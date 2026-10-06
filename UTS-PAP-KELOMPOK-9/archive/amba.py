import random
def jawaban_salah(jawaban_benar):
    salah1 = jawaban_benar + random.randint(1,4)
    salah2 = jawaban_benar - random.randint(1,4)
    salah3 = jawaban_benar + random.randint(5,8)

    if salah2 <=0:
        salah2=jawaban_benar + random.randint(9,12)

    return salah1,salah2,salah3

print(type(jawaban_salah(1)))