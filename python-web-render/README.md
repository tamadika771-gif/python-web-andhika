# Web Python Pertamaku — Flask + Render

Aplikasi web kecil untuk belajar Flask. Halaman utama menerima nama melalui formulir, lalu menampilkan sapaan. Endpoint `/health` mengembalikan status server dalam format JSON.

## Isi folder

- `app.py` — kode server Flask.
- `templates/index.html` — halaman website.
- `requirements.txt` — paket Python yang dipasang saat deploy.
- `render.yaml` — konfigurasi Blueprint Render (opsional).

## 1. Menjalankan di Windows

Buka PowerShell di folder project ini. Buat dan aktifkan virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Untuk menjalankan secara lokal di Windows, pasang Flask lalu mulai server:

```powershell
python -m pip install Flask
python app.py
```

Buka `http://127.0.0.1:5000` di browser. Endpoint pemeriksaan status: `http://127.0.0.1:5000/health`.

`gunicorn` di `requirements.txt` diperlukan oleh Render di Linux; server lokal Windows dijalankan dengan `python app.py`.

## 2. Mengirim project ke GitHub dengan Git

Buat repository baru di GitHub, misalnya `python-web-andhika`. Agar langkah push sederhana, buat repository kosong (jangan centang pilihan untuk menambahkan README).

Di PowerShell, pastikan terminal berada di folder project, lalu jalankan:

```powershell
git init
git add .
git commit -m "Buat web Flask pertama"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

Ganti `USERNAME` dan `REPO` sesuai alamat repository milikmu. Jika Git meminta login, selesaikan autentikasi di browser. Jangan pernah menaruh password atau access token GitHub di dalam file kode.

Jika perintah `git` tidak dikenali, pasang Git for Windows atau gunakan aplikasi GitHub Desktop untuk menerbitkan folder project ke repository.

## 3. Deploy dari GitHub ke Render

1. Masuk ke Render dan pilih masuk/terhubung dengan akun GitHub.
2. Di Render, pilih **New + → Web Service**.
3. Hubungkan repository `python-web-andhika` (atau nama repository yang kamu buat).
4. Atur layanan:
   - **Language/Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Instance Type/Plan:** Free
5. Pilih **Deploy Web Service**. Setelah build berhasil, Render akan memberikan URL seperti `https://nama-layanan.onrender.com`.
6. Tes URL tersebut dan tambahkan `/health` untuk memeriksa endpoint status.

Render juga dapat membaca `render.yaml`: pilih **New + → Blueprint**, hubungkan repository, lalu tinjau dan terapkan konfigurasi yang ditemukan. Pilih salah satu cara deploy saja; Web Service manual biasanya paling mudah diikuti pertama kali.

Setelah repository terhubung, perubahan yang kamu push ke branch yang dipilih dapat memicu deploy ulang otomatis.

## Catatan tentang hosting gratis

Render Free cocok untuk belajar dan demo, tetapi web service dapat tidur setelah 15 menit tanpa trafik dan mungkin perlu sekitar satu menit untuk aktif kembali saat dibuka. Jadi, opsi gratis ini tidak menjamin server aktif tanpa henti 24 jam. Untuk layanan yang benar-benar penting, gunakan paket hosting berbayar atau server yang memiliki jaminan uptime.
