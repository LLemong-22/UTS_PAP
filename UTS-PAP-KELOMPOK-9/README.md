# 🏰 Tower of MATH1011

> **Tugas Proyek UTS - Pengantar Algoritma dan Pemrograman**  
> **Kelompok 9** | Aplikasi Kuis Matematika Pilihan Ganda Berbasis CLI (Terminal)

---

## 👥 Anggota Kelompok

| No | Nama Lengkap | NIM |
| :-: | :--- | :---: |
| 1 | **Wilbert Owen Nathanael** | 262602544 |
| 2 | **Christoph Jordan Dalimartin** | 262510530 |
| 3 | **Lionel Esra Mailuhu** | 262602117 |
| 4 | **Joel Sebastian Lasmito** | 262415411 |
| 5 | **Evan Adhiarja Yohanes** | 262407793 |
| 6 | **Yosia Edmund Herlianto** | 262514949 |

---

## 🎮 Tentang Game

**Tower of MATH1011** adalah game kuis matematika seru bertema RPG yang dimainkan lewat terminal (CLI). 

Di game ini, kamu bermain sebagai seorang petualang yang mendaki menara misterius setinggi **11 Lantai**. Di setiap lantai, kamu harus menjawab soal matematika pilihan ganda (A, B, C, D) untuk mengalahkan monster dan mengumpulkan kepingan emas (**Gold**).

- **Lantai 1 – 10 (Monster Matematika):**  
  Berisi soal matematika dasar: penjumlahan (+), pengurangan (-), perkalian (*), dan pembagian pas (/).  
  Tiap jawaban benar mendapat **+10 Gold**.
- **Lantai 11 (Final Boss - Sangar PhD):**  
  Pertarungan puncak melawan dosen penguji bernama **Sangar PhD** dengan soal cerita RPG (menghitung jumlah putaran untuk menghabisi HP Boss).  
  Jika berhasil menjawab benar, kamu mendapat **+911 Gold**!
- **Maksimal Gold:**  
  Jika semua soal terjawab benar, total Gold yang didapat adalah **1011 Gold** (100 + 911), sesuai dengan nama menara ini: **MATH1011**!

> **Catatan:**  
> Jika jawabanmu salah di suatu lantai, kamu tidak mendapat Gold (0 Gold), tetapi petualangan tetap lanjut sampai lantai 11!

---

## 🏆 Kategori Skor Akhir

Di akhir permainan, total Gold yang kamu kumpulkan akan menentukan gelar petualanganmu:

| Total Gold | Gelar Petualang | Keterangan |
| :---: | :--- | :--- |
| **1011 Gold** | 👑 **Penakluk Super Sangar** | Menjawab semua soal dengan benar dan membawa pulang seluruh harta karun! |
| **911 – 1001 Gold** | ⚔️ **Penakluk Sangar** | Berhasil mengalahkan Final Boss di lantai 11 dan membawa pulang harta terbesar. |
| **10 – 100 Gold** | 🛡️ **Kurang Sangar** | Berhasil mengumpulkan Gold dari monster biasa, tapi belum berhasil mengalahkan Final Boss. |
| **0 Gold** | 💀 **Tidak Sangar** | Gagal menjawab semua soal di menara. |

---

## 🚀 Cara Menjalankan Game

Pastikan komputer kamu sudah terpasang **Python 3**.

1. **Buka Terminal / Command Prompt**, lalu masuk ke folder ini:
   ```bash
   cd UTS-PAP-KELOMPOK-9
   ```

2. **Jalankan game dengan perintah:**
   ```bash
   python3 main.py
   ```
   *(atau `python main.py` di Windows)*

3. **Cara Bermain:**  
   - Baca soal dan 4 pilihan jawaban yang muncul (A, B, C, atau D).
   - Ketik huruf pilihanmu lalu tekan **Enter**.
   - Input tidak sensitif huruf besar/kecil (bisa ketik `a` atau `A`).
   - Kumpulkan Gold sebanyak-banyaknya hingga lantai 11!

---

## 📁 Struktur File

```text
UTS-PAP-KELOMPOK-9/
├── main.py                        <- Program utama game Tower of MATH1011
├── TEAM.md                        <- Dokumen rancangan tim
├── README.md                      <- Panduan proyek ini
├── flowchart/
│   └── flowchart_game.md          <- Diagram alur program (Mermaid)
├── report/
│   ├── LAPORAN_PROYEK.md          <- Laporan resmi proyek UTS
│   └── konsep awal.png            <- Gambar konsep awal permainan
└── archive/                       <- Catatan pembagian tugas anggota tim
```

---

## 💡 Konsep Kode

Program ini dibuat khusus untuk memenuhi materi perkuliahan **Dasar Pemrograman (Week 1–7)**:
- Menggunakan logika murni: variabel, tipe data skalar (angka dan teks), percabangan (`if-elif-else`), perulangan (`for` dan `while`), serta fungsi bawaan (`def`).
- **Tanpa struktur data koleksi** (tidak menggunakan `list`, `dict`, `set`, atau `tuple`) sesuai aturan batas materi.
- Dilengkapi validasi input agar program tidak mudah error saat user salah mengetik.
