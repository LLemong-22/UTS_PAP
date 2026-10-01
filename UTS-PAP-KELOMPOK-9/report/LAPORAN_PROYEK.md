Project Coding: Tower of MATH1011
UTS - Pengantar Algoritma dan Pemrograman
Anggota Kelompok 9 (Aplikasi kuis matematika pilihan ganda (ada skor akhir)):
Wilbert Owen Nathanael (262602544)
Christoph Jordan Dalimartin (262510530)
Lionel Esra Mailuhu (262602117)
Joel Sebastian Lasmito (262415411)
Evan Adhiarja Yohanes (262407793)
Yosia Edmund Herlianto (262514949)
1. Konsep & Ide Game
Di game ini, user bakal berperan jadi seorang petualang yang lagi mendaki menara misterius bernama Tower of MATH1011. Tujuan utamanya simpel banget: kumpulin Gold sebanyak-banyaknya dengan cara menjawab kuis matematika pilihan ganda yang dijaga sama monster-monster matematika di tiap lantai.
Tujuan Utama: Murni cuman ngumpulin Gold
Mekanisme Lantai: Kalau jawabanmu benar, kamu dapat 10 Gold dan naik ke lantai berikutnya. Kalau salah, kamu nggak dapet Gold (0 Gold), tapi tetap lanjut naik sampai ke lantai 11.
Final Boss: Begitu sampai lantai 11, kamu akan dihadang oleh final boss bernama “Sangar PhD”. menjawab soalnya (jika benar akan mendapatkan 911 Gold)
ENDING: total Gold yang kamu kumpulkan bakal dihitung buat nentuin seberapa "sangar" petualangan kita.

2. Fitur Utama Program
Kuis matematika yang digamify jadi seperti main game
Tantangan Final Boss (Soal Cerita / Logika): Lantai 11 menghadirkan soal cerita yang berbeda dengan soal di lantai biasa
Sistem Akumulasi Skor (kita pakai Gold): Jawaban benar memberi +10 Gold di lantai reguler dan +911 Gold di lantai boss, dengan target skor maksimal 1011 Gold.
Tampilan skor akhir: Diakhir ada output evaluasi pencapaian petualang di akhir permainan berdasarkan total Gold yang berhasil dikumpulkan.

3. Struktur Lantai & Sistem Gold
Menara ini punya total 11 Lantai (11 Soal) dengan pembagian hadiah sebagai berikut:
Lantai 1 – 10 (Monster Aritmatika Dasar)
Soal: Penjumlahan (+), pengurangan (-), perkalian (*), dan pembagian(/).
Hadiah: 10 Gold per soal yang dijawab benar.
Maksimal Gold: 100 Gold.
Lantai 11 (FINAL BOSS: Sangar PhD)
Soal cerita tingkat lanjut
Hadiah: 911 Gold.
Kalau kamu berhasil jawab semua soal dengan benar, kamu bakal dapet total 1011 Gold (100 + 911), sesuai judul projectnya: MATH1011!

Total Gold
Gelar / Kategori
Keterangan
1011 Gold
Penakluk Super Sangar
Menjawab seluruh soal dengan benar tanpa cela dan menjarah seluruh harta karun menara.
911 – 1001 Gold
Penakluk Sangar
Berhasil menaklukkan Final Boss di lantai 11 dan membawa pulang rampasan harta terbesar.
10 – 100 Gold
Kurang Sangar
Berhasil mengumpulkan Gold dari monster biasa, namun gagal menaklukkan tantangan lantai 11.
0 Gold
Tidak Sangar
Gagal menjawab seluruh pertanyaan di setiap lantai menara.


Tampilan Game (CLI)
==================================================
      SELAMAT DATANG DI TOWER OF MATH1011      
  Kumpulkan kepingan Gold dan taklukkan Puncak!
==================================================


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
5.1. Tampilan Final Boss (Lantai 11)
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
5.2. Tampilan Skor Akhir - jawab benar semua
==================================================
              HASIL EKSPEDISI TOWER              
==================================================
Total Gold yang Dikumpulkan : 1011 / 1011 Gold
Kategori Petualang          : Penakluk Super Sangar
Pesan Petualangan           : Ekspedisi selesai! Anda berhasil
                              membawa pulang seluruh harta karun
                              dari Tower of MATH1011!
==================================================

