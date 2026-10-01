# DOKUMEN PEMBAGIAN TUGAS KODE (REVERSE ENGINEERING & INTEGRASI)
## PROJECT 9: TOWER OF MATH1011 (UTS PAP KELOMPOK 9)

Dokumen ini membedah kode program utuh menjadi **6 modul kode independen** sehingga **seluruh anggota kelompok (6 orang) berkontribusi langsung pada baris kode program (`main.py`)**. Masing-masing anggota bertanggung jawab atas fungsinya, dapat mengujinya secara mandiri (*standalone unit test*), dan menggabungkannya kembali ke file utama [main.py](file:///home/lemong/Projects/UTS_PAP/UTS-PAP-KELOMPOK-9/main.py).

---

### PEMETAAN ANGGOTA & BAGIAN KODE

| Task | Nama Modul Kode | Penanggung Jawab | Fungsi dalam Kode |
| :-: | :--- | :--- | :--- |
| **Task 1** | Generator Soal Aritmatika Dasar (Lantai 1–10) | **Wilbert Owen Nathanael** (262602544) | `generate_soal_reguler()` |
| **Task 2** | Fungsi Validasi Input & Handling Sanitasi String | **Christoph Jordan Dalimartin** (262510530) | `validasi_input_jawaban()` |
| **Task 3** | Algoritma Distraktor & Pengacakan Opsi A/B/C/D | **Lionel Esra Mailuhu** (262602117) | `buat_distraktor()`, `tampilkan_pilihan()` |
| **Task 4** | Generator Final Boss & Simulasi Tempur RPG (Lantai 11) | **Joel Sebastian Lasmito** (262415411) | `generate_soal_boss()` |
| **Task 5** | Modul Rekapitulasi Akhir & Evaluasi Matriks Gold | **Evan Adhiarja Yohanes** (262407793) | `tampilkan_hasil_ekspedisi()` |
| **Task 6** | Generator Nama Monster & Controller Loop Utama Game | **Yosia Edmund Herlianto** (262514949) | `buat_nama_monster()`, `main()` |

---

## 📌 TASK 1 — Generator Soal Aritmatika Dasar (Lantai 1–10)
**Penanggung Jawab:** Wilbert Owen Nathanael (262602544)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `generate_soal_reguler()`:
  - Mengacak 4 tipe operasi matematika dasar: Penjumlahan (`+`), Pengurangan (`-`), Perkalian (`*`), dan Pembagian Bulat (`//`).
  - Menjamin hasil pengurangan tidak negatif (`if a < b: swap`).
  - Menjamin pembagian selalu bulat sempurna tanpa sisa pecahan (`hasil_kali = a * b`, `tanya = f"{hasil_kali} // {b} = ?"`).
  - Mengembalikan 4 nilai skalar: `nama_monster, teks_soal, jawaban_benar, HADIAH_GOLD_REGULER`.

### Potongan Kode yang Dikerjakan:
```python
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
```

### Cara Pengujian Mandiri (Standalone Test):
```python
# Tes fungsi secara terisolasi
import random
HADIAH_GOLD_REGULER = 10
def buat_nama_monster(): return "Monster Uji Coba"

monster, soal, kunci, gold = generate_soal_reguler()
print(f"Monster: {monster} | Soal: {soal} | Kunci: {kunci} | Hadiah: {gold} Gold")
```

---

## 📌 TASK 2 — Fungsi Validasi Input & Handling Sanitasi String
**Penanggung Jawab:** Christoph Jordan Dalimartin (262510530)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `validasi_input_jawaban(prompt_teks)`:
  - Sanitasi string: menghapus whitespace tak sengaja via `.strip()` dan mengubah ke huruf besar via `.upper()`.
  - Loop validasi boolean: menolak semua karakter kecuali `'A'`, `'B'`, `'C'`, atau `'D'`.
  - Murni tanpa tipe data koleksi (`list`/`set`/`dict`), mencegah program error saat user mengetik sembarang input.

### Potongan Kode yang Dikerjakan:
```python
def validasi_input_jawaban(prompt_teks):
    """
    Menerima input pengguna, melakukan sanitasi string (.strip() dan .upper()),
    serta memvalidasi pilihan hanya A, B, C, atau D tanpa struktur list.
    """
    jawaban = input(prompt_teks).strip().upper()
    while jawaban != "A" and jawaban != "B" and jawaban != "C" and jawaban != "D":
        print(">> Pilihan tidak valid! Harap masukkan hanya A, B, C, atau D.")
        jawaban = input(prompt_teks).strip().upper()
    return jawaban
```

### Cara Pengujian Mandiri (Standalone Test):
```python
# Tes validasi input dengan memasukkan huruf kecil 'a', spasi '  b  ', atau karakter salah 'x'
hasil = validasi_input_jawaban("Tes Jawaban (A/B/C/D): ")
print(f"Input berhasil diterima dan disanitasi: '{hasil}'")
```

---

## 📌 TASK 3 — Algoritma Distraktor & Pengacakan Posisi Opsi (A/B/C/D)
**Penanggung Jawab:** Lionel Esra Mailuhu (262602117)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `buat_distraktor(jawaban_benar)`:
  - Menghitung 3 nilai opsi salah skalar (`salah1`, `salah2`, `salah3`) yang dekat dengan kunci jawaban dan dijamin unik tanpa collision.
  - Menjamin nilai distraktor selalu positif (> 0).
- Membuat fungsi `tampilkan_pilihan(posisi_benar, benar, s1, s2, s3)`:
  - Menerima posisi acak 1 sampai 4.
  - Mencetak baris pilihan A, B, C, D murni menggunakan percabangan `if-elif-else`.
  - Mengembalikan huruf opsi yang menjadi kunci jawaban.

### Potongan Kode yang Dikerjakan:
```python
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
```

### Cara Pengujian Mandiri (Standalone Test):
```python
import random
s1, s2, s3 = buat_distraktor(25)
print(f"Kunci: 25 | Pengecoh: {s1}, {s2}, {s3}")
kunci_huruf = tampilkan_pilihan(3, 25, s1, s2, s3)
print(f"Kunci yang harusnya di C: {kunci_huruf}")
```

---

## 📌 TASK 4 — Generator Final Boss & Simulasi Tempur RPG (Lantai 11)
**Penanggung Jawab:** Joel Sebastian Lasmito (262415411)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `generate_soal_boss()` dari skenario RPG `test.ipynb`:
  - Mengatur Final Boss: **SANGAR PhD (Dosen Penguji MATH1011)**.
  - Simulasi matematika putaran tempur (turns):
    - Target putaran acak `total_putaran` (40–60 putaran, bukan kelipatan 4).
    - Menghitung HP Boss berdasarkan formula DMG pemain, Regen Boss, dan skill pasif *Divine Shield* (tiap kelipatan 4 putaran, DMG pemain = 0 tapi Boss tetap regen).
  - Mengembalikan: `nama_monster, teks_soal, jawaban_benar, HADIAH_GOLD_BOSS`.

### Potongan Kode yang Dikerjakan:
```python
def generate_soal_boss():
    nama_monster = "SANGAR PhD (Dosen Penguji MATH1011)"

    total_putaran = random.randint(40, 60)
    while total_putaran % 4 == 0:
        total_putaran = random.randint(40, 60)

    dmg_player = random.randint(1500, 2500)
    heal_boss = random.randint(200, 500)

    hp_calc = 0
    for r in range(1, total_putaran + 1):
        if r % 4 == 0:
            hp_calc += heal_boss
        else:
            hp_calc += (dmg_player - heal_boss)

    hp_boss = hp_calc - random.randint(1, (dmg_player - heal_boss) - 1)
    jawaban_benar = total_putaran

    teks_soal = (
        f"SANGAR PhD turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss        : {hp_boss:,}\n"
        f"- DMG Senjatamu  : {dmg_player:,} / putaran\n"
        f"- Regen Boss     : {heal_boss:,} HP tiap diserang\n"
        f"- Pasif Shield   : Tiap kelipatan 4 putaran, DMG senjata = 0 (Boss tetap regen)!\n\n"
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?"
    )

    return nama_monster, teks_soal, jawaban_benar, HADIAH_GOLD_BOSS
```

### Cara Pengujian Mandiri (Standalone Test):
```python
import random
HADIAH_GOLD_BOSS = 911
nama, soal, kunci, gold = generate_soal_boss()
print(f"--- {nama} ---")
print(soal)
print(f"Kunci Jawaban yang Benar: {kunci} putaran (+{gold} Gold)")
```

---

## 📌 TASK 5 — Modul Rekapitulasi Akhir & Evaluasi Matriks Gold
**Penanggung Jawab:** Evan Adhiarja Yohanes (262407793)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `tampilkan_hasil_ekspedisi(total_gold)`:
  - Menghitung dan mengevaluasi perolehan kepingan emas akhir ke dalam kategori PRD `TEAM.md`:
    - **1011 Gold:** Penakluk Super Sangar
    - **911 – 1001 Gold:** Penakluk Sangar
    - **10 – 100 Gold:** Kurang Sangar
    - **0 Gold:** Tidak Sangar
  - Mencetak kotak antarmuka ASCII (*CLI summary screen*) yang presisi dan rapi.

### Potongan Kode yang Dikerjakan:
```python
def tampilkan_hasil_ekspedisi(total_gold):
    print("==================================================")
    print("              HASIL EKSPEDISI TOWER               ")
    print("==================================================")
    print(f"Total Gold yang Dikumpulkan : {total_gold} / {TOTAL_GOLD_MAKSIMAL} Gold")

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
```

### Cara Pengujian Mandiri (Standalone Test):
```python
TOTAL_GOLD_MAKSIMAL = 1011
# Uji coba untuk 4 kategori skor berbeda:
tampilkan_hasil_ekspedisi(1011) # Super Sangar
tampilkan_hasil_ekspedisi(951)  # Sangar
tampilkan_hasil_ekspedisi(50)   # Kurang Sangar
tampilkan_hasil_ekspedisi(0)    # Tidak Sangar
```

---

## 📌 TASK 6 — Generator Nama Monster & Controller Loop Utama Game
**Penanggung Jawab:** Yosia Edmund Herlianto (262514949)

### Deskripsi & Tanggung Jawab:
- Membuat fungsi `buat_nama_monster()`:
  - Menggabungkan nama tim (Owen, Christoph, Lionel, Joel, Evan, Yosia) dengan materi kalkulus/matematika Indonesia (Asimtot, Garis Singgung, Limit, Turunan, Integral, Diferensial) murni memakai `if-elif-else` skalar.
- Membuat fungsi controller `main()`:
  - Mengelola variabel akumulasi `total_gold = 0`.
  - Loop 11 lantai (`for lantai in range(1, TOTAL_LANTAI + 1)`).
  - Merajut dan memanggil seluruh modul rekan-rekan: generator soal reguler (Task 1), distraktor & opsi (Task 3), validasi input (Task 2), soal boss (Task 4), serta layar rekapitulasi akhir (Task 5).

### Potongan Kode yang Dikerjakan:
```python
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
            print(f"[FLOOR {lantai} / {TOTAL_LANTAI}] | TOTAL SAKU: {total_gold} GOLD")
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
```
