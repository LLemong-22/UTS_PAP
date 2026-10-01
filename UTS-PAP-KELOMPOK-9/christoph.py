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