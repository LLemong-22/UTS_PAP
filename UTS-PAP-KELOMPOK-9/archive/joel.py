import random

def generate_soal_boss():
    nama_monster = "SANGAR PhD (Dosen Penguji MATH1011)"
    
    # Total putaran (bukan kelipatan 4)
    total_putaran = random.randint(40, 60)
    while total_putaran % 4 == 0:
        total_putaran = random.randint(40, 60)
    
    # Status boss & player
    dmg_player = random.randint(1500, 2500)
    heal_boss = random.randint(200, 500)
    
    # === HITUNG HP BOSS ===
    # Aturan:
    # - Putaran kelipatan 4: DMG player = 0, boss regen (heal_boss)
    # - Putaran lain: DMG player masuk, boss regen (heal_boss)
    
    hp_calc = 0
    for r in range(1, total_putaran + 1):
        if r % 4 == 0:
            # Boss tidak kena damage, tapi regen
            hp_calc += heal_boss
        else:
            # Boss kena damage, tapi juga regen
            hp_calc += (dmg_player - heal_boss)
    
    # Kasih variasi HP boss (biar tidak selalu pas)
    hp_boss = hp_calc - random.randint(1, (dmg_player - heal_boss) - 1)
    
    # Jawaban benar
    jawaban_benar = total_putaran
    
    # Teks soal
    teks_soal = (
        f"{nama_monster} turun ke medan perang dengan aura mematikan!\n"
        f"Status Pertarungan:\n"
        f"- HP Boss        : {hp_boss:,}\n"
        f"- DMG Senjatamu  : {dmg_player:,} / putaran\n"
        f"- Regen Boss     : {heal_boss:,} HP tiap diserang\n"
        f"- Pasif Shield   : Tiap kelipatan 4 putaran, DMG senjata = 0 (Boss tetap regen)!\n\n"
        f"Pertanyaan: Berapa putaran yang kamu butuhkan untuk menghabisi HP Boss sampai 0?"
    )
    
    return nama_monster, teks_soal, jawaban_benar