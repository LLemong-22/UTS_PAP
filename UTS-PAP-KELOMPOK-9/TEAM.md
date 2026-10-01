## UTS - Pengantar Algoritma dan Pemrograman
# KELOMPOK :
- Wilbert Owen Nathanael (262602544)
- Christoph Jordan Dalimartin (262510530)
- Lionel Esra Mailuhu (262602117)
- Joel Sebastian Lasmito (262415411)
- Evan Adhiarja Yohanes (262407793)
- Yosia Edmund Herlianto (262514949)

## PROJECT - 9. Aplikasi kuis matematika pilihan ganda (ada skor akhir)
## PROJECT - 9. Aplikasi Kuis Matematika Pilihan Ganda (Tower of MATH1011)

### 1. Konsep & Narasi Game

Pemain berperan sebagai petualang yang mendaki **Tower of MATH1011** untuk berburu harta karun berupa kepingan emas (*Gold*). Setiap lantai menghadirkan tantangan monster matematika dalam format pilihan ganda.

* **Fokus Mekanisme:** Akumulasi total *Gold* murni (tanpa sistem HP dan tanpa status kelulusan akademis/KKM).
* **Alur Lantai:** Menjawab benar menghasilkan *Gold* dan pemain langsung lanjut ke lantai berikutnya. Menjawab salah tidak memberikan hadiah (0 *Gold*), namun pemain tetap melanjutkan perjalanan hingga puncak menara.
* **Hasil Akhir:** Di akhir permainan, sistem murni menampilkan akumulasi total *Gold* yang berhasil dikumpulkan oleh petualang.

---

### 2. Struktur Lantai & Perolehan Gold

Terdapat total **11 Lantai (11 Soal)**:

* **Lantai 1 – 10 (Monster Aritmatika Dasar):**
* Tipe Operasi: Penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), dan pembagian bulat (`//`).
* Hadiah: **10 Gold per soal benar**.
* Maksimal Gold Lantai Reguler: **100 Gold**.


* **Lantai 11 (FINAL BOSS: Monster Aljabar / Soal Lanjutan):**
* Tipe Operasi: Perhitungan matematika tingkat lanjut dengan formula khusus memanfaatkan modul bawaan `math`.


* Hadiah: **911 Gold**.


* **Total Gold Maksimal:** **1011 Gold** ($100 + 911$), merepresentasikan angka kode menara **MATH1011**.

---

### 3. Matriks Hasil Perolehan Akhir (*Gold Summary*)

| Total Gold Diperoleh | Kategori Pencapaian | Keterangan Petualangan |
| --- | --- | --- |
| **1011 Gold** | **Penakluk Super Sangar** | Menjawab seluruh soal dengan benar tanpa cela dan menjarah seluruh harta karun menara. |
| **911 – 1001 Gold** | **Penakluk Sangar** | Berhasil menaklukkan Final Boss di lantai 11 dan membawa pulang rampasan harta terbesar. |
| **10 – 100 Gold** | **Kurang Sangar** | Berhasil mengumpulkan *Gold* dari monster biasa, namun gagal menaklukkan tantangan lantai 11. |
| **0 Gold** | **Tidak Sangar** | Gagal menjawab seluruh pertanyaan di setiap lantai menara. |

---

### 4. Batasan Teknis & Arsitektur Kode

Sesuai batasan materi perkuliahan **Week 1 sampai 7 (Introduction hingga Functions)**:

* **Dilarang Menggunakan Tipe Data Koleksi:** Tidak menggunakan struktur data `list`, `dict`, `set`, maupun `tuple`.


* **Generator Distraktor:** Nilai opsi pengecoh dibangkitkan secara acak melalui fungsi skalar `buat_distraktor()`.
* **Pengacakan Letak Opsi:** Penempatan kunci jawaban pada pilihan A, B, C, atau D diacak via integer (1–4) dan dicetak melalui struktur percabangan `if-elif-else` pada fungsi `tampilkan_pilihan()`.
* **Modul:** Murni mengandalkan pustaka standar bawaan Python: `random` dan `math`.

---

### 5. Rancangan Tampilan Terminal (CLI Interface)

**Tampilan Lantai Reguler (Lantai 1 – 10)**

```text
==================================================
[FLOOR 4 / 11] | TOTAL SAKU: 30 GOLD
Monster Perkalian menghadang jalanmu!
==================================================
Pertanyaan: 12 * 7 = ?
A. 84
B. 81
C. 86
D. 90
Jawaban Anda (A/B/C/D): A

>> TEPAT SEKALI! Monster kalah, Anda memperoleh +10 Gold!

```

**Tampilan Lantai 11 (Final Boss)**

```text
==================================================
>>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<
>>> FINAL BOSS: THE GUARDIAN OF MATH1011 <<<
Hadiah Kemenangan: 911 GOLD
==================================================
Pertanyaan: Berapakah hasil dari (6^2 + 8^2) - 4 ?
A. 92
B. 96
C. 100
D. 104
Jawaban Anda (A/B/C/D): B

>> LUAR BIASA! FINAL BOSS DIKALAHKAN, Anda memperoleh +911 Gold!

```

**Tampilan Layar Skor Akhir**

```text
==================================================
              HASIL EKSPEDISI TOWER               
==================================================
Total Gold yang Dikumpulkan : 1011 / 1011 Gold
Kategori Petualang          : Grand Champion (Harta Sempurna)
Pesan Petualangan           : Ekspedisi selesai! Anda berhasil 
                              membawa pulang seluruh harta karun 
                              dari Tower of MATH1011!
==================================================

```