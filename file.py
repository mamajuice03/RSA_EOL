from PyPDF2 import PdfWriter, PdfReader

# buat objek pdf writer
out = PdfWriter()

# buka file pdf asli
file = PdfReader("D:\D3 Teknik Informatika\Semester 3\Praktik Sistem Keamanan Data\TUGAS SKD FULL\RSA\File\Testing.pdf")

# identifikasi total halaman file
num = len(file.pages)

# program membaca setiap halaman file sesuai halaman yang diidentifikasi
for idx in range(num):
    page = file.pages[idx]
    out.add_page(page)

# masukkan password enkripsi
password = "test123"

# enkripsi masing-masing halaman
out.encrypt(password)

# buka file enkripsi "myfile_encrypted.pdf"
with open("TestingPW.pdf", "wb") as f:  # Open a new file to write the encrypted PDF
    # simpan pdf
    out.write(f)
