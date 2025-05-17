# WebFTP

Aplikasi berbasis web untuk mengelola file melalui FTP, mirip dengan WinSCP tetapi dengan tampilan web yang sederhana.

## Fitur

- **Penjelajahan File FTP**: Menjelajahi direktori dan file di server FTP
- **Editor Kode**: Mengedit file kode sumber dengan syntax highlighting
- **Preview Website**: Melihat preview file HTML dan gambar
- **Manajemen File**: Unggah, unduh, dan hapus file
- **Manajemen Direktori**: Buat dan hapus direktori

## Persyaratan

- Python 3.6+
- Flask
- pyftpdlib
- dan dependensi lainnya (lihat requirements.txt)

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/username/WebFTP.git
   cd WebFTP
   ```

2. Buat dan aktifkan virtual environment (opsional):
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instal dependensi:
   ```
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:
   ```
   python app.py
   ```

5. Buka browser dan akses aplikasi di `http://localhost:9000`

## Penggunaan

1. **Login FTP**: Masukkan host, port, username, dan password FTP Anda
2. **Jelajahi File**: Setelah login, Anda dapat menjelajahi file dan direktori
3. **Edit File**: Klik tombol "Edit" pada file yang ingin diedit
4. **Preview**: Klik tombol "Lihat" pada file HTML untuk melihat preview
5. **Unggah File**: Klik tombol "Unggah File" dan pilih file dari komputer Anda
6. **Buat Direktori**: Klik tombol "Buat Direktori" dan masukkan nama direktori baru

## Keamanan

Aplikasi ini menggunakan koneksi FTP standar yang tidak dienkripsi. Jangan gunakan untuk file sensitif atau di jaringan tidak aman. Untuk keamanan lebih baik, pertimbangkan untuk menggunakan SFTP atau FTPS.

## Lisensi

Lisensi MIT. Lihat file LICENSE untuk detail lebih lanjut. 

by Saputra Budi