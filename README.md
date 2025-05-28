# Gikes Bot (Clone dari @darenankesbot)

Bot Telegram ini adalah clone dari @darenankesbot, dibuat dengan Pyrogram dan MongoDB. Bot ini memiliki fitur-fitur seperti anti-gcast, blacklist kata dan pengguna, daftar pengguna tanpa dosa, dan kontrol akses berbasis peran (owner, sudo).

## Cara Menjalankan

1.  **Prasyarat:**
    * Python 3.7 atau lebih tinggi terinstal.
    * pip terinstal.
    * Akses ke server MongoDB.
    * Token Bot Telegram dari BotFather.
    * `API_ID` dan `API_HASH` dari Telegram Core ([https://my.telegram.org/apps](https://my.telegram.org/apps)).

2.  **Klon atau Buat Struktur Direktori:**
    * Anda dapat mengunduh proyek ini sebagai ZIP atau menggunakan `git clone [URL_REPOSITORY_ANDA]` jika Anda menghostingnya di GitHub.
    * Jika tidak, buat struktur direktori seperti yang dijelaskan dalam dokumentasi.

3.  **Buat dan Aktifkan Virtual Environment (Disarankan):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Di Linux/macOS
    # venv\Scripts\activate   # Di Windows
    ```

4.  **Instal Dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Konfigurasi Bot:**
    * Buat file `.env` di direktori utama proyek (`gikes/`).
    * Salin isi dari `sample.env` ke dalam `.env`.
    * Ganti semua nilai placeholder dengan informasi bot dan database Anda yang sebenarnya.

6.  **Jalankan Bot:**
    ```bash
    chmod +x start  # Berikan izin eksekusi pada script start (Linux/macOS)
    ./start        # Jalankan bot
    ```
    Atau:
    ```bash
    bash start      # Jalankan bot
    ```

## Fitur

* **Anti Gcast:** Mampu menghapus pesan forward dari channel tertentu (perlu konfigurasi lebih lanjut).
* **Blacklist Kata:** Mencegah dan menghapus pesan yang mengandung kata-kata yang diblacklist.
* **Blacklist Pengguna:** Memblokir tindakan dari pengguna yang diblacklist.
* **Daftar Pengguna Tanpa Dosa (Free User):** Pengguna yang berada dalam daftar ini mungkin dikecualikan dari beberapa pembatasan.
* **Kontrol Akses Berbasis Peran:**
    * **Owner:** Pemilik bot dengan akses penuh.
    * **Sudo User:** Pengguna dengan akses ke perintah administratif tertentu.
    * **Admin Group Owner:** (Implementasi terbatas, perlu pengembangan lebih lanjut).
* **Menu Utama:** Akses fitur-fitur dasar bot melalui tombol inline.
* **Menu Bantuan:** Daftar perintah dan deskripsi bot.
* **Tombol "Masukan Gua Ke Group":** Link langsung untuk menambahkan bot ke grup.
* **Tombol "Owner":** Mengarah ke profil pemilik bot.

## Perintah (Contoh)

* `/start`: Memulai bot dan menampilkan menu utama.
* `Help`: Menampilkan menu bantuan.
* `Owner`: Menampilkan informasi pemilik bot.
* `Close`: Menutup keyboard.
* `/ankes on`: Mengaktifkan fitur Ankes (memerlukan izin owner/sudo).
* `/ankes off`: Menonaktifkan fitur Ankes (memerlukan izin owner/sudo).
* `/addfree [user_id]`: Menambahkan pengguna ke daftar tanpa dosa (memerlukan izin owner).
* `/delfree [user_id]`: Menghapus pengguna dari daftar tanpa dosa (memerlukan izin owner).
* `/addbl [kata]`: Menambahkan kata ke blacklist (memerlukan izin owner/sudo).
* `/delbl [kata]`: Menghapus kata dari blacklist (memerlukan izin owner/sudo).
* `/listbl`: Melihat daftar kata yang diblacklist (memerlukan izin owner/sudo).
* `/addblack [reply]`: Menambahkan pengguna yang dibalas ke blacklist (memerlukan izin owner/sudo).
* `/delblack [user_id]`: Menghapus pengguna dari blacklist (memerlukan izin owner/sudo).
* `/getbl`: Melihat daftar pengguna yang diblacklist (memerlukan izin owner/sudo).
* `/promote [user_id] [owner|sudo|free|admin]`: Mengatur peran pengguna (memerlukan izin owner).

**Catatan:** Daftar perintah mungkin tidak lengkap dan dapat bervariasi tergantung pada pengembangan lebih lanjut.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori dan kirimkan pull request dengan perubahan yang Anda buat.

## Lisensi

[MIT License](LICENSE) (Jika Anda ingin menambahkan lisensi)