# Tugas Akhir Pengolahan Citra Digital (PCD)
**Topik:** Traditional Image-Based Vehicle Detection
**Kelompok 2:**
1. Ahmad Ramadhan Shobrunjamil (24051204168)
2. Muhammad Anwar Ismail (24051204161)

## 📌 Jurnal Referensi
**Judul:** *A Hybrid Approach for Real-time Vehicle Monitoring System (IJEM, 2024)*
**Penulis:** Pankaj Pratap Singh, Shitala Prasad
**Link Jurnal:** [https://www.mecs-press.org/ijem/ijem-v14-n1/v14n1-1.html](https://www.mecs-press.org/ijem/ijem-v14-n1/v14n1-1.html)

---

## 🛠️ Penjelasan Metode yang Digunakan
Program ini sepenuhnya ditulis dari awal menggunakan **Pengolahan Citra Tradisional** tanpa menggunakan *library Deep Learning* / *Machine Learning* (Seperti YOLO atau CNN). 

Program ini mempraktikkan langsung **6 materi presentasi dosen**, antara lain:
1. **Dasar Citra Digital (Slide 01 & 02):** Membaca video lalu lintas sebagai barisan matriks *frame*.
2. **Pengolahan Citra Berwarna (Slide 05):** Mengubah *frame* RGB (Berwarna) menjadi *Grayscale* (Abu-abu) untuk mempermudah perhitungan komputasi.
3. **Peningkatan Kualitas Citra / Image Subtracting (Slide 03):** Mengurangi (*subtraction*) *frame* pertama dengan *frame* berikutnya untuk mendeteksi adanya objek yang bergerak (dalam hal ini kendaraan/mobil).
4. **Spatial Filtering & Thresholding (Slide 04):** Melakukan penghalusan (*Gaussian Blur*) dan mengubah warna hasil *subtracting* menjadi biner (hitam-putih mutlak) menggunakan *Thresholding*.
5. **Morfologi Citra (Slide 06):** Menggunakan teknik **Dilasi** (*Dilation*) untuk menebalkan bagian putih pada mobil yang terputus, sehingga badan mobil terlihat menyatu sepenuhnya.

---

## 🚀 Cara Menjalankan Program

### 1. Persiapan Kebutuhan (Requirements)
Pastikan laptop/komputer Anda sudah terinstal Python. Buka terminal atau Command Prompt (CMD), lalu jalankan perintah ini untuk menginstal *library* yang dibutuhkan:
```bash
pip install opencv-python numpy
```

### 2. File yang Dibutuhkan
Pastikan di dalam satu folder, terdapat dua file berikut:
- `deteksi_kendaraan.py` (File *Source Code* Python)
- `traffic.mp4` (Video sampel jalan raya)

### 3. Menjalankan Program (Running)
Buka terminal/CMD di dalam folder, lalu ketikkan perintah berikut:
```bash
python deteksi_kendaraan.py
```

### 4. Navigasi Program
Saat program berjalan, akan muncul **3 jendela terpisah** yang menunjukkan proses pengolahan citra dari awal hingga akhir. 
- Untuk **MENUTUP / KELUAR** dari program, pastikan Anda mengklik salah satu jendela video tersebut, lalu tekan tombol **ESC** pada keyboard.
