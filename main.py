# Membuat kamus sandi Morse
kamus_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Fungsi untuk mengenkripsi pesan dengan sandi Morse
def enkripsi_morse(pesan):
    pesan = pesan.upper()
    pesan_terenkripsi = ''
    for karakter in pesan:
        if karakter != ' ':
            pesan_terenkripsi += kamus_morse[karakter] + ' '
        else:
            pesan_terenkripsi += ' '
    return pesan_terenkripsi

# Fungsi untuk mendekripsi pesan dengan sandi Morse
def dekripsi_morse(pesan):
    pesan_terdekripsi = ''
    pesan = pesan.split(' ')
    for kode in pesan:
        if kode != '':
            for huruf, morse in kamus_morse.items():
                if morse == kode:
                    pesan_terdekripsi += huruf
        else:
            pesan_terdekripsi += ' '
    return pesan_terdekripsi

# Meminta input pesan dari pengguna
pesan = input("Masukkan pesan yang ingin dienkripsi/didekripsi: ")

# Meminta input tipe operasi (enkripsi/mendekripsi)
operasi = input("Pilih tipe operasi (E: enkripsi, D: dekripsi): ")

# Memanggil fungsi enkripsi atau dekripsi sesuai dengan tipe operasi yang dipilih
if operasi.upper() == 'E':
    pesan_terenkripsi = enkripsi_morse(pesan)
    print("Pesan terenkripsi:", pesan_terenkripsi)
elif operasi.upper() == 'D':
    pesan_terdekripsi = dekripsi_morse(pesan)
    print("Pesan terdekripsi:", pesan_terdekripsi)
else:
    print("Tipe operasi tidak valid.")

# andhika pratama p
