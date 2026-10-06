# Dokumen Rancangan Tim - Tower of MATH1011
**Tugas Proyek UTS - Pengantar Algoritma dan Pemrograman**  
**Kelompok 9 | Aplikasi Kuis Matematika Pilihan Ganda (Ada Skor Akhir)**

---

### Anggota Kelompok 9:
- Wilbert Owen Nathanael (262602544)
- Christoph Jordan Dalimartin (262510530)
- Lionel Esra Mailuhu (262602117)
- Joel Sebastian Lasmito (262415411)
- Evan Adhiarja Yohanes (262407793)
- Yosia Edmund Herlianto (262514949)

---

### 1. Konsep & Narasi Game

Pemain berperan sebagai petualang yang mendaki **Tower of MATH1011** untuk berburu harta karun berupa kepingan emas (*Gold*). Setiap lantai menghadirkan tantangan monster matematika dalam format pilihan ganda.

* **Fokus Mekanisme:** Akumulasi total *Gold* murni (tanpa sistem HP petualang dan tanpa status kelulusan akademis/KKM).
* **Alur Lantai:** Menjawab benar menghasilkan *Gold* dan pemain langsung lanjut ke lantai berikutnya. Menjawab salah tidak memberikan hadiah (0 *Gold*), namun pemain tetap melanjutkan perjalanan hingga puncak menara.
* **Hasil Akhir:** Di akhir permainan, sistem murni menampilkan akumulasi total *Gold* yang berhasil dikumpulkan oleh petualang.

---

### 2. Struktur Lantai & Perolehan Gold

Terdapat total **11 Lantai (11 Soal)**:

* **Lantai 1 – 10 (Monster Aritmatika Dasar):**
  * Tipe Operasi: Penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), dan pembagian bulat (`//`).
  * Hadiah: **10 Gold per soal benar**.
  * Maksimal Gold Lantai Reguler: **100 Gold**.

* **Lantai 11 (FINAL BOSS: SANGAR PhD - Dosen Penguji MATH1011):**
  * Tipe Operasi: Soal cerita tingkat lanjut (kalkulasi putaran tempur menghabisi HP Boss: membagi total HP Boss dengan DMG Senjata per putaran).
  * Hadiah: **911 Gold**.

* **Total Gold Maksimal:** **1011 Gold** ($100 + 911$), merepresentasikan angka kode menara **MATH1011**.

---

### 3. Matriks Hasil Perolehan Akhir (*Gold Summary*)

| Total Gold Diperoleh | Kategori Pencapaian | Keterangan Petualangan |
| :---: | :--- | :--- |
| **1011 Gold** | **Penakluk Super Sangar** | Menjawab seluruh soal dengan benar tanpa cela dan menjarah seluruh harta karun menara. |
| **911 – 1001 Gold** | **Penakluk Sangar** | Berhasil menaklukkan Final Boss di lantai 11 dan membawa pulang rampasan harta terbesar. |
| **10 – 100 Gold** | **Kurang Sangar** | Berhasil mengumpulkan *Gold* dari monster biasa, namun gagal menaklukkan tantangan lantai 11. |
| **0 Gold** | **Tidak Sangar** | Gagal menjawab seluruh pertanyaan di setiap lantai menara. |

---

### 4. Batasan Teknis & Arsitektur Kode

Sesuai batasan materi perkuliahan **Week 1 sampai 7 (Introduction hingga Functions)**:

* **Dilarang Menggunakan Tipe Data Koleksi:** Tidak menggunakan struktur data `list`, `dict`, `set`, maupun `tuple`. Setiap fungsi hanya mengembalikan satu nilai skalar tunggal.
* **Generator Distraktor:** Nilai opsi pengecoh dibangkitkan secara acak melalui fungsi skalar `jawaban_salah(jawaban_benar, urutan)` dengan rentang non-overlapping untuk mencegah duplikasi.
* **Pengacakan Letak Opsi:** Penempatan kunci jawaban pada pilihan A, B, C, atau D diacak via integer (1–4) dan dicetak melalui struktur percabangan `if-elif-else` pada fungsi `pilihan_jawaban()`.
* **Sanitasi & Validasi Input:** Validasi input pengguna memanfaatkan loop `while` serta sanitasi `.strip().upper()` agar aman dari variasi huruf atau spasi.
* **Modul:** Murni mengandalkan pustaka standar bawaan Python: `random`.

---

### 5. Rancangan Tampilan Terminal (CLI Interface)

**Tampilan Lantai Reguler (Lantai 1 – 10)**

```text
==================================================
[FLOOR 1 / 11] | TOTAL GOLD: 0 GOLD
Monster Christoph Limit menghadang jalanmu!
==================================================
Pertanyaan: Serang titik lemahnya dengan menjawab: 14 * 4 = ?
A. 56
B. 58
C. 53
D. 61
Jawaban Anda (A/B/C/D): A

>> CRITICAL HIT! Monster Christoph Limit kalah, Anda memperoleh +10 Gold!
```

**Tampilan Lantai 11 (Final Boss)**

```text
==================================================
>>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<
>>> FINAL BOSS: SANGAR PhD (Dosen Penguji MATH1011) <<<
Hadiah Kemenangan: 911 GOLD
==================================================
SANGAR PhD turun ke medan perang dengan aura mematikan!
Status Pertarungan:
- HP Boss        : 57,684
- DMG Senjatamu  : 1,748 / putaran

Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?
A. 35
B. 33
C. 32
D. 41
Jawaban Anda (A/B/C/D): B

>> FATALITY! SANGAR PhD (Dosen Penguji MATH1011) DIKALAHKAN, Anda memperoleh +911 Gold!
```

**Tampilan Layar Skor Akhir**

```text
==================================================
              HASIL EKSPEDISI TOWER               
==================================================
Total Gold yang Dikumpulkan : 1011 / 1011 Gold
Kategori Petualang          : Penakluk Super Sangar
Pesan Petualangan           : Ekspedisi selesai! Anda berhasil 
                              membawa pulang seluruh harta karun 
                              dari Tower of MATH1011!
==================================================
```