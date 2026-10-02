import random

def generate_soal_boss():
    """
    Task 4: Joel Sebastian Lasmito (262415411)
    Membangkitkan soal Final Boss (Lantai 11) - SANGAR PhD
    """
    nama_monster = "SANGAR PhD (Dosen Penguji MATH1011)"
    
    # Total putaran tempur
    total_putaran = random.randint(20, 50)
    dmg_player = random.randint(1500, 2500)
    hp_boss = total_putaran * dmg_player
    jawaban_benar = total_putaran
    
    # Teks soal
    teks_soal = (
        f"{nama_monster} turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss        : {hp_boss:,}\n"
        f"- DMG Senjatamu  : {dmg_player:,} / putaran\n\n"
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?"
    )
    
    return nama_monster, teks_soal, jawaban_benar, 911