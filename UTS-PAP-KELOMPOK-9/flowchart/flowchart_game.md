# Dokumentasi Flowchart Sistem - Tower of MATH1011
**Kelompok 9 | Pengantar Algoritma dan Pemrograman (PAP)**

---

## Diagram Alir Utama (Game Flowchart)

Diagram alir berikut memetakan logika eksekusi program `main.py` dari awal hingga selesai, mencakup lantai reguler (1–10), simulasi pertarungan Final Boss (Lantai 11), dan modul rekapitulasi akhir:

```mermaid
flowchart TD
    Start([Mulai]) --> Init["total_gold = 0<br/>lantai = 1"]
    Init --> LoopLantai{"lantai <= 11 ?"}

    %% Cabang Lantai Reguler vs Boss
    LoopLantai -- Ya --> CekLantai{"lantai <= 10 ?"}

    %% Sub-alur Lantai Reguler (1-10)
    subgraph LantaiReguler["Lantai Reguler (1 - 10)"]
        CekLantai -- Ya --> GenReguler["Buat Nama Monster & Soal Aritmatika (+, -, *, //)<br/>Swap jika pengurangan & a < b"]
        GenReguler --> HitungReguler["Hitung Jawaban Benar & Generate Distraktor (s1, s2, s3)"]
        HitungReguler --> AcakReguler["Acak Posisi Kunci (1..4)"]
        AcakReguler --> TampilReguler[/"Tampilkan Header Lantai, Soal & Opsi (A, B, C, D)"/]
        TampilReguler --> InputReguler[/"Input & Validasi Jawaban User (A/B/C/D)"/]
        InputReguler --> CekJawabanReguler{"Jawaban User == Kunci ?"}
        CekJawabanReguler -- Benar --> WinReguler[/"Tampilkan Critical Hit! Pesan Berhasil"/]
        WinReguler --> AddGoldReguler["total_gold += 10"]
        CekJawabanReguler -- Salah --> LoseReguler[/"Tampilkan Serangan Meleset & Kunci Jawaban"/]
    end

    %% Sub-alur Final Boss (Lantai 11)
    subgraph FinalBoss["Final Boss Lantai 11 (SANGAR PhD)"]
        CekLantai -- Tidak --> InitBoss["Inisialisasi Status Pertarungan:<br/>total_putaran = random(20, 50)<br/>dmg_player = random(1500, 2500)<br/>hp_boss = total_putaran * dmg_player<br/>jawaban_benar = total_putaran"]
        InitBoss --> SetKunciBoss["Generate Distraktor (s1, s2, s3)<br/>Acak Posisi Kunci (1..4)"]
        SetKunciBoss --> TampilBoss[/"Tampilkan Status Pertarungan, Soal Cerita & Opsi (A, B, C, D)"/]
        TampilBoss --> InputBoss[/"Input & Validasi Jawaban User (A/B/C/D)"/]
        InputBoss --> CekJawabanBoss{"Jawaban User == Kunci ?"}
        CekJawabanBoss -- Benar --> WinBoss[/"Tampilkan Fatality! SANGAR PhD Dikalahkan"/]
        WinBoss --> AddGoldBoss["total_gold += 911"]
        CekJawabanBoss -- Salah --> LoseBoss[/"Tampilkan You Died! & Kunci Jawaban"/]
    end

    %% Next Lantai
    AddGoldReguler --> NextFloor["lantai = lantai + 1"]
    LoseReguler --> NextFloor
    AddGoldBoss --> NextFloor
    LoseBoss --> NextFloor
    NextFloor --> LoopLantai

    %% Rekapitulasi Akhir
    subgraph RekapitulasiSkor["Penentuan Kategori & Skor Akhir"]
        LoopLantai -- Tidak --> Cek1011{"total_gold == 1011 ?"}
        Cek1011 -- Ya --> Kat1["Kategori: Penakluk Super Sangar"]
        Cek1011 -- Tidak --> Cek911{"total_gold >= 911 ?"}
        Cek911 -- Ya --> Kat2["Kategori: Penakluk Sangar"]
        Cek911 -- Tidak --> Cek10{"total_gold >= 10 ?"}
        Cek10 -- Ya --> Kat3["Kategori: Kurang Sangar"]
        Cek10 -- Tidak --> Kat4["Kategori: Tidak Sangar"]
        Kat1 --> TampilRekap[/"Cetak Ringkasan Ekspedisi & Gelar Petualang"/]
        Kat2 --> TampilRekap
        Kat3 --> TampilRekap
        Kat4 --> TampilRekap
    end

    TampilRekap --> End([Selesai])
```
