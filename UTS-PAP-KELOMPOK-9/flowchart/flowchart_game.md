# DOKUMENTASI FLOWCHART SISTEM - TOWER OF MATH1011
**Kelompok 9 - Pengantar Algoritma dan Pemrograman (PAP)**

---

## 1. Diagram Alir Utama (Game Flowchart)

Diagram ini mengilustrasikan seluruh alur eksekusi program `main.py` dari inisialisasi hingga kalkulasi hasil akhir.

```mermaid
flowchart TD
    Start([Mulai]) --> Init[Inisialisasi Konstanta & total_gold = 0]
    Init --> LoopStart{Lantai <= 11 ?}

    %% Cabang Kondisi Lantai
    LoopStart -- Ya --> CekLantai{Lantai <= 10 ?}
    
    CekLantai -- Ya (Lantai 1-10) --> GenReguler[generate_soal_reguler<br/>Panggil buat_nama_monster anggota tim & mtk<br/>Acak operasi +, -, *, // & hitung bobot = 10]
    CekLantai -- Tidak (Lantai 11) --> GenBoss[generate_soal_boss<br/>Kalkulasi putaran tempur RPG test.ipynb<br/>Hitung jawaban_benar & bobot = 911]

    GenReguler --> DisplayHeader[Tampilkan Header Lantai & Monster]
    GenBoss --> DisplayHeaderBoss[Tampilkan Header Final Boss SANGAR PhD]

    DisplayHeader --> Distraktor[buat_distraktor<br/>Bentuk 3 jawaban salah s1, s2, s3 skalar]
    DisplayHeaderBoss --> Distraktor

    Distraktor --> AcakPosisi[Acak posisi kunci: random 1..4]
    AcakPosisi --> CetakOpsi[tampilkan_pilihan<br/>Cetak A/B/C/D via if-elif-else<br/>Simpan huruf kunci jawaban]

    %% Validasi Input Pengguna
    CetakOpsi --> InputUser[/Input jawaban_user/]
    InputUser --> Sanitasi[Sanitasi string: .strip.upper]
    Sanitasi --> Validasi{Jawaban in 'A', 'B', 'C', 'D'?}
    Validasi -- Tidak Valid --> PesanError[Tampilkan Pesan Error Validasi]
    PesanError --> InputUser
    
    %% Evaluasi Jawaban
    Validasi -- Valid --> CekJawaban{jawaban_user == kunci ?}
    CekJawaban -- Benar --> TambahGold[total_gold += bobot<br/>Tampilkan Pesan Berhasil & Perolehan Gold]
    CekJawaban -- Salah --> PesanSalah[Tampilkan Pesan Meleset & Kunci Jawaban Benar]

    TambahGold --> NextFloor[Lantai = Lantai + 1]
    PesanSalah --> NextFloor
    NextFloor --> LoopStart

    %% Rekapitulasi Akhir
    LoopStart -- Selesai (Lantai > 11) --> TampilRekap[tampilkan_hasil_ekspedisi<br/>Evaluasi total_gold ke Matriks Pencapaian]
    TampilRekap --> CetakSkor[/Cetak Box HASIL EKSPEDISI TOWER/]
    CetakSkor --> End([Selesai])
```

---

## 2. Penjelasan Komponen Alur (Traceability ke Task Tim)

| Simbol / Tahapan | Fungsi / Modul Terkait | Penanggung Jawab Task |
| :--- | :--- | :--- |
| **Generator Soal Reguler (Lantai 1-10)** | `generate_soal_reguler()` | **Task 1: Wilbert Owen Nathanael** |
| **Validasi & Sanitasi Input Jawaban** | `validasi_input_jawaban()` | **Task 2: Christoph Jordan Dalimartin** |
| **Distraktor & Tampilan Opsi A/B/C/D** | `buat_distraktor()`, `tampilkan_pilihan()` | **Task 3: Lionel Esra Mailuhu** |
| **Generator Final Boss (Lantai 11)** | `generate_soal_boss()` | **Task 4: Joel Sebastian Lasmito** |
| **Rekapitulasi Akhir & Matriks Gold** | `tampilkan_hasil_ekspedisi()` | **Task 5: Evan Adhiarja Yohanes** |
| **Generator Nama Monster & Game Loop** | `buat_nama_monster()`, `main()` | **Task 6: Yosia Edmund Herlianto** |
