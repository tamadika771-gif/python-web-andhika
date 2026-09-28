"""Web app Flask sederhana untuk belajar dan dideploy ke Render."""

import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    nama = ""
    if request.method == "POST":
        # Ambil nama dari formulir dan batasi panjangnya.
        nama = request.form.get("nama", "").strip()[:60]
    return render_template("index.html", nama=nama)


@app.get("/health")
def health():
    """Endpoint sederhana untuk memeriksa apakah server aktif."""
    return {"status": "ok", "app": "python-dasar-web"}, 200


if __name__ == "__main__":
    # Untuk percobaan lokal di komputer sendiri.
    # Saat di Render, Gunicorn yang menjalankan aplikasi ini.
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)
