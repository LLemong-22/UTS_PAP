# LAPORAN TUGAS PROYEK UTS
## PENGANTAR ALGORITMA DAN PEMROGRAMAN (PAP)
### PROJECT CODING: TOWER OF MATH1011 (APLIKASI KUIS MATEMATIKA PILIHAN GANDA)

---

### Disusun Oleh Kelompok 9:
1. **Wilbert Owen Nathanael** (262602544)
2. **Christoph Jordan Dalimartin** (262510530)
3. **Lionel Esra Mailuhu** (262602117)
4. **Joel Sebastian Lasmito** (262415411)
5. **Evan Adhiarja Yohanes** (262407793)
6. **Yosia Edmund Herlianto** (262514949)

---

## 1. TENTANG PROYEK (KONSEP & IDE GAME)

### 1.1 Deskripsi Game
Di game ini, pemain (*user*) bakal berperan sebagai seorang petualang pemberani yang sedang mendaki menara misterius bernama **Tower of MATH1011**. 

Tujuan utamanya simpel banget: **kumpulin kepingan emas (*Gold*) sebanyak-banyaknya** dengan cara menaklukkan kuis matematika pilihan ganda yang dijaga oleh monster-monster di setiap lantai!

* **Fokus Mekanisme Permainan:** Murni tentang akumulasi *Gold* (tanpa sistem HP/nyawa dan tanpa sistem nilai kelulusan akademis/KKM yang bikin stres).
* **Alur Perjalanan Lantai:** 
  * Kalau jawabanmu **benar**, kamu mendapatkan kepingan *Gold* (+10 Gold di lantai biasa) dan langsung naik ke lantai berikutnya.
  * Kalau jawabanmu **salah**, kamu tidak mendapatkan hadiah (0 Gold), tapi jangan khawatir: perjalananmu tidak langsung tamat (*no game over*), melainkan kamu tetap bisa lanjut naik menara sampai tiba di puncak!
* **Final Boss:** Begitu sampai di lantai 11, petualang akan dihadang oleh penguasa puncak menara: **Sangar PhD (Dosen Penguji MATH1011)** dengan soal tantangan cerita kalkulasi tempur tingkat lanjut!
* **Ending Permainan:** Di akhir ekspedisi menara, sistem akan menghitung akumulasi total *Gold* yang berhasil kamu bawa pulang untuk menentukan gelar dan seberapa **"Sangar"** petualanganmu!

---

## 2. STRUKTUR LANTAI & SISTEM GOLD

Menara ini memiliki total **11 Lantai (11 Soal)** dengan pembagian tantangan dan perolehan harta karun sebagai berikut:

### 🔹 Lantai 1 – 10 (Monster Aritmatika Dasar)
* **Tipe Soal:** Operasi matematika dasar yang mencakup penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), dan pembagian bulat (`//`).
* **Hadiah:** **10 Gold per soal** yang dijawab dengan benar.
* **Maksimal Gold Lantai Reguler:** **100 Gold** (10 soal $\times$ 10 Gold).

### 🔹 Lantai 11 (FINAL BOSS: Sangar PhD)
* **Tipe Soal:** Soal cerita kalkulasi tempur RPG tingkat lanjut (*Boss Fight*) yang melibatkan perhitungan giliran tempur (*turns*), *damage* senjata, *health regeneration* boss, dan pasif kebal *Divine Shield*.
* **Hadiah:** **911 Gold**.

### 🔹 Akumulasi Total & Simbolik Menara
Jika pemain berhasil menjawab seluruh pertanyaan di setiap lantai dengan benar, pemain akan mengantongi total:
$$\mathbf{100\ Gold} + \mathbf{911\ Gold} = \mathbf{1011\ Gold}$$
Angka **1011 Gold** ini melambangkan kode menara sekaligus kode mata kuliah: **MATH1011**!

---

### 📊 Matriks Kategori Hasil Akhir (*Gold Summary*)

| Total Gold Diperoleh | Gelar / Kategori | Keterangan Petualangan |
| :---: | :---: | :--- |
| **1011 Gold** | **Penakluk Super Sangar** | Menjawab seluruh soal dengan benar tanpa cela dan menjarah seluruh harta karun menara. |
| **911 – 1001 Gold** | **Penakluk Sangar** | Berhasil menaklukkan Final Boss di lantai 11 dan membawa pulang rampasan harta terbesar. |
| **10 – 100 Gold** | **Kurang Sangar** | Berhasil mengumpulkan *Gold* dari monster biasa, namun gagal menaklukkan tantangan lantai 11. |
| **0 Gold** | **Tidak Sangar** | Gagal menjawab seluruh pertanyaan di setiap lantai menara. |

---

## 3. FITUR-FITUR UTAMA APLIKASI

Aplikasi *Tower of MATH1011* dirancang dengan sejumlah fitur unggulan yang membuat pengalaman bermain seru, interaktif, dan bebas dari kendala teknis:

1. **Sistem Menara 11 Lantai & Real-Time Gold Tracker:**
   Di setiap lantai, layar menampilkan nomor lantai yang sedang dihadapi serta jumlah total *Gold* yang sudah berhasil terkumpul di kantong pemain.
2. **Generator Nama Monster Lucu & Unik (Anggota Tim + Materi Matematika):**
   Monster yang menghadang petualang diacak secara dinamis dengan menggabungkan nama panggilan anggota tim kelompok 9 (Owen, Christoph, Lionel, Joel, Evan, Yosia) dengan istilah kalkulus/matematika Indonesia (Asimtot, Garis Singgung, Limit, Turunan, Integral, Diferensial). Contoh: *Monster Owen Asimtot*, *Monster Christoph Limit*, atau *Monster Joel Garis Singgung*.
3. **Generator Soal Dinamis & Angka Bulat Presisi:**
   Soal aritmatika diacak tiap kali program dijalankan. Khusus pembagian bulat (`//`), sistem menjamin hasilnya selalu bilangan bulat rapi tanpa sisa desimal. Untuk pengurangan, sistem menjamin hasilnya non-negatif.
4. **Final Boss Fight dengan Mekanik RPG Menantang:**
   Pertarungan lantai 11 bukan sekadar hitung-hitungan biasa, melainkan simulasi RPG teka-teki giliran tempur dengan status HP Boss puluhan ribu, *damage* senjata, regenerasi HP, dan pasif kebal *Divine Shield* setiap kelipatan 4 putaran.
5. **Anti-Crash Input Validation & String Sanitizer:**
   Sistem tahan banting terhadap kesalahan ketik. Pengguna yang memasukkan huruf kecil (`a`, `b`, dll) atau spasi ekstra (`  A  `) otomatis disanitasi menjadi kapital bersih. Jika pemain memasukkan karakter ilegal (seperti angka atau simbol), program tidak akan *crash*, melainkan menampilkan pesan edukatif dan meminta input ulang sampai valid.
6. **Algoritma Distraktor Cerdas & Bebas Tipe Data Koleksi:**
   Pilihan pengecoh A, B, C, D dibangkitkan secara matematis dengan selisih acak yang mendekati jawaban asli serta dijamin tidak ada pilihan kembar (*no collision*), dibangun 100% murni tanpa menggunakan tipe data koleksi (`list`, `dict`, `set`, `tuple`) sesuai silabus Week 1–7.
7. **Layar Rekapitulasi Akhir Dinamis:**
   Di akhir game, sistem mencetak kotak laporan hasil ekspedisi ASCII yang elegan dan mengelompokkan pencapaian pemain ke dalam matriks gelar petualang yang sesuai.

---

## 4. PEMBAGIAN TUGAS KODE TIM (REVERSE ENGINEERING)

Setiap anggota kelompok 9 memiliki kontribusi nyata berupa fungsi mandiri di dalam berkas [main.py](file:///home/lemong/Projects/UTS_PAP/UTS-PAP-KELOMPOK-9/main.py):

| Task | Penanggung Jawab | Fungsi dalam Kode | Tanggung Jawab Modul |
| :-: | :--- | :--- | :--- |
| **Task 1** | **Wilbert Owen Nathanael** (262602544) | `generate_soal_reguler()` | Generator 4 operasi aritmatika dasar (`+`, `-`, `*`, `//`), pembagian bulat sempurna, dan kalkulasi jawaban benar berbobot 10 Gold. |
| **Task 2** | **Christoph Jordan Dalimartin** (262510530) | `validasi_input_jawaban()` | Sanitasi string (`.strip().upper()`) dan perulangan `while` validasi boolean tanpa `list` agar program anti-crash. |
| **Task 3** | **Lionel Esra Mailuhu** (262602117) | `buat_distraktor()`, `tampilkan_pilihan()` | Algoritma pembentuk 3 distraktor skalar unik non-nol dan perender opsi pilihan ganda A/B/C/D via `if-elif-else`. |
| **Task 4** | **Joel Sebastian Lasmito** (262415411) | `generate_soal_boss()` | Generator Final Boss Sangar PhD dengan simulasi putaran pertempuran RPG, HP puluhan ribu, dan pasif Divine Shield (+911 Gold). |
| **Task 5** | **Evan Adhiarja Yohanes** (262407793) | `tampilkan_hasil_ekspedisi()` | Evaluasi 4 kategori gelar petualang dan pencetakan antarmuka kotak hasil ekspedisi (*summary screen*). |
| **Task 6** | **Yosia Edmund Herlianto** (262514949) | `buat_nama_monster()`, `main()` | Generator nama monster gabungan tim & istilah matematika serta loop utama 11 lantai yang mengorkestrasi semua modul. |

---

## 5. FLOWCHART SISTEM

*(Dokumentasi diagram alir visual lengkap dengan diagram Mermaid dan traceability kode dapat dilihat pada berkas terpisah: [flowchart/flowchart_game.md](file:///home/lemong/Projects/UTS_PAP/UTS-PAP-KELOMPOK-9/flowchart/flowchart_game.md)).*

### Ringkasan Logika Alur Program:
1. **Mulai & Inisialisasi:** Program menginisialisasi konstanta aturan menara dan variabel akumulator `total_gold = 0`.
2. **Loop Menara (Lantai 1 s/d 11):**
   * Jika Lantai 1–10: Panggil `generate_soal_reguler()`, tampilkan nama monster hasil kombinasi acak dan soal matematika dasar.
   * Jika Lantai 11: Tampilkan peringatan Final Boss dan panggil `generate_soal_boss()`.
3. **Penyusunan Opsi Pilihan Ganda:**
   * Bangkitkan 3 distraktor via `buat_distraktor()`.
   * Acak letak kunci jawaban (posisi 1–4) dan cetak pilihan A, B, C, D via `tampilkan_pilihan()`.
4. **Input & Validasi:**
   * Ambil jawaban pemain lewat `validasi_input_jawaban()`.
   * Bersihkan spasi dan ubah ke kapital. Jika di luar A/B/C/D, cetak peringatan dan minta input ulang.
5. **Evaluasi & Akumulasi Skor:**
   * Jika jawaban cocok dengan kunci: Tambahkan Gold (+10 atau +911) dan cetak pesan keberhasilan.
   * Jika salah: Tambahkan 0 Gold dan tampilkan kunci yang tepat.
6. **Rekapitulasi Akhir:**
   * Setelah lantai 11 selesai, panggil `tampilkan_hasil_ekspedisi()` untuk mencetak kotak hasil ekspedisi dan gelar petualang sesuai total perolehan Gold.
7. **Selesai.**

---

## 6. CONTOH OUTPUT TAMPILAN TERMINAL (CLI)

Berikut adalah contoh output nyata hasil eksekusi program di terminal dalam berbagai kondisi permainan:

### 🎮 Output 1: Pembuka Permainan & Lantai Reguler (Jawaban Benar)
```text
==================================================
      SELAMAT DATANG DI TOWER OF MATH1011       
  Kumpulkan kepingan Gold dan taklukkan Puncak! 
==================================================

==================================================
[FLOOR 1 / 11] | TOTAL SAKU: 0 GOLD
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

---

### 🎮 Output 2: Lantai Reguler Saat Serangan Meleset (Jawaban Salah)
```text
==================================================
[FLOOR 3 / 11] | TOTAL SAKU: 20 GOLD
Monster Owen Asimtot menghadang jalanmu!
==================================================
Pertanyaan: Serang titik lemahnya dengan menjawab: 18 // 3 = ?
A. 8
B. 6
C. 4
D. 10
Jawaban Anda (A/B/C/D): A

>> SERANGAN MELESET! Kunci jawaban yang tepat adalah B.
```

---

### 🎮 Output 3: Penanganan Input Salah / Tidak Valid (Fitur Validasi & Sanitasi)
Jika pemain salah ketik (misalnya mengetik angka, spasi sembarangan, atau karakter acak), sistem menolak dengan aman tanpa *crash*:
```text
==================================================
[FLOOR 5 / 11] | TOTAL SAKU: 30 GOLD
Monster Joel Garis Singgung menghadang jalanmu!
==================================================
Pertanyaan: Serang titik lemahnya dengan menjawab: 15 + 9 = ?
A. 22
B. 24
C. 28
D. 21
Jawaban Anda (A/B/C/D): x
>> Pilihan tidak valid! Harap masukkan hanya A, B, C, atau D.
Jawaban Anda (A/B/C/D): 12
>> Pilihan tidak valid! Harap masukkan hanya A, B, C, atau D.
Jawaban Anda (A/B/C/D):   b  

>> CRITICAL HIT! Monster Joel Garis Singgung kalah, Anda memperoleh +10 Gold!
```
*(Catatan: Input `'  b  '` dengan huruf kecil dan spasi berhasil disanitasi otomatis menjadi `'B'` yang sah).*

---

### 🎮 Output 4: Pertarungan Puncak Lantai 11 (FINAL BOSS: Sangar PhD)
```text
==================================================
>>> PERINGATAN: ANDA MEMASUKI LANTAI 11 <<<
>>> FINAL BOSS: SANGAR PhD (Dosen Penguji MATH1011) <<<
Hadiah Kemenangan: 911 GOLD
==================================================
SANGAR PhD turun ke medan perang dengan aura mematikan!
Status Pertarungan:
- HP Boss        : 58,420
- DMG Senjatamu  : 2,120 / putaran
- Regen Boss     : 340 HP tiap diserang
- Pasif Shield   : Tiap kelipatan 4 putaran, DMG senjata = 0 (Boss tetap regen)!

Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?
A. 47
B. 44
C. 42
D. 50
Jawaban Anda (A/B/C/D): A

>> FATALITY! SANGAR PhD (Dosen Penguji MATH1011) DIKALAHKAN, Anda memperoleh +911 Gold!
```

---

### 🎮 Output 5: Layar Rekap Skor Akhir - Kategori "Penakluk Super Sangar" (1011 Gold)
*(Kondisi saat petualang menjawab seluruh soal dari lantai 1 sampai 11 dengan benar murni)*:
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

---

### 🎮 Output 6: Layar Rekap Skor Akhir - Kategori "Penakluk Sangar" (911 - 1001 Gold)
*(Kondisi saat petualang berhasil mengalahkan Final Boss, namun sempat melewatkan beberapa soal biasa)*:
```text
==================================================
              HASIL EKSPEDISI TOWER               
==================================================
Total Gold yang Dikumpulkan : 971 / 1011 Gold
Kategori Petualang          : Penakluk Sangar
Pesan Petualangan           : Berhasil menaklukkan Final Boss di lantai 11
                              dan membawa pulang rampasan harta terbesar.
==================================================
```

---

### 🎮 Output 7: Layar Rekap Skor Akhir - Kategori "Kurang Sangar" (10 - 100 Gold)
*(Kondisi saat petualang mengumpulkan poin dari monster biasa, namun kalah di hadapan Sangar PhD)*:
```text
==================================================
              HASIL EKSPEDISI TOWER               
==================================================
Total Gold yang Dikumpulkan : 60 / 1011 Gold
Kategori Petualang          : Kurang Sangar
Pesan Petualangan           : Berhasil mengumpulkan Gold dari monster biasa,
                              namun gagal menaklukkan tantangan lantai 11.
==================================================
```

---

### 🎮 Output 8: Layar Rekap Skor Akhir - Kategori "Tidak Sangar" (0 Gold)
*(Kondisi saat petualang salah menjawab di seluruh lantai menara)*:
```text
==================================================
              HASIL EKSPEDISI TOWER               
==================================================
Total Gold yang Dikumpulkan : 0 / 1011 Gold
Kategori Petualang          : Tidak Sangar
Pesan Petualangan           : Gagal menjawab seluruh pertanyaan di setiap
                              lantai menara.
==================================================
```

---

## 7. CARA MENJALANKAN GAME

Untuk memainkan game petualangan matematika ini, ikuti langkah mudah berikut di terminal komputer:

1. Buka terminal dan arahkan ke direktori proyek:
   ```bash
   cd UTS-PAP-KELOMPOK-9
   ```
2. Jalankan berkas utama menggunakan Python 3:
   ```bash
   python3 main.py
   ```
3. Selamat mendaki menara dan raih gelar **Penakluk Super Sangar**!

---

## 8. KESIMPULAN

Proyek game **Tower of MATH1011** berhasil membuktikan bahwa materi dasar pemrograman prosedural (variabel skalar, percabangan `if-elif-else`, perulangan `while`/`for`, dan fungsi modular) dapat dikemas menjadi sebuah game petualangan yang interaktif, menyenangkan, dan edukatif. 

Meskipun mematuhi batasan ketat tanpa tipe data koleksi (`list`, `dict`, `set`, `tuple`), arsitektur yang dirancang secara gotong royong oleh seluruh anggota Kelompok 9 tetap mampu menyajikan permainan yang kaya fitur, tahan terhadap kesalahan input pengguna, dan memiliki alur cerita yang hidup.
