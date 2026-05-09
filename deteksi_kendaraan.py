import cv2
import numpy as np

# 1. Buka video lalu lintas (Pastikan Anda punya file 'traffic.mp4' di folder yang sama)
# Anda bisa mendownload video jalan raya gratis dari YouTube atau Pexels.
cap = cv2.VideoCapture('traffic.mp4')

# Baca 2 frame pertama untuk dibandingkan
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Pastikan frame berhasil dibaca
    if not ret or frame2 is None:
        break
        
    # =========================================================================
    # TAHAP 1: IMAGE SUBTRACTING (Sesuai Materi Slide 03)
    # =========================================================================
    # Mengurangi Frame 1 dengan Frame 2 untuk mencari objek yang bergerak
    diff = cv2.absdiff(frame1, frame2)
    
    # =========================================================================
    # TAHAP 2: PENGOLAHAN CITRA BERWARNA (Sesuai Materi Slide 05)
    # =========================================================================
    # Mengubah citra RGB (berwarna) menjadi Grayscale (Abu-abu)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # =========================================================================
    # TAHAP 3: SPATIAL FILTERING & HISTOGRAM (Sesuai Materi Slide 04)
    # =========================================================================
    # Menggunakan Gaussian Blur untuk menghaluskan gambar (menghilangkan noise kecil)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Melakukan Thresholding biner (piksel terang jadi putih mutlak, gelap jadi hitam mutlak)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # =========================================================================
    # TAHAP 4: MORFOLOGI CITRA (Sesuai Materi Slide 06)
    # =========================================================================
    # Menggunakan DILASI untuk menebalkan bercak putih (mobil) yang terputus agar menyatu
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # =========================================================================
    # TAHAP 5: PENGGAMBARAN KOTAK (Bounding Box)
    # =========================================================================
    # Mencari kontur/garis luar dari bercak putih
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    output_frame = frame1.copy()

    for contour in contours:
        # Filter ukuran: Jika bercak putih terlalu kecil (< 700 piksel), abaikan
        if cv2.contourArea(contour) < 700:
            continue
            
        # Dapatkan koordinat (x, y) serta lebar dan tinggi untuk menggambar kotak
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Gambar kotak hijau pada gambar asli
        cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output_frame, "Kendaraan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Tampilkan 3 Jendela untuk presentasi ke Dosen
    cv2.imshow("1. Hasil Threshold (Hitam Putih)", thresh)
    cv2.imshow("2. Hasil Morfologi (Dilasi)", dilated)
    cv2.imshow("3. Hasil Deteksi Kendaraan", output_frame)
    
    # Geser frame (Frame 2 menjadi Frame 1, lalu baca frame baru untuk Frame 2)
    frame1 = frame2
    ret, frame2 = cap.read()

    # Tekan 'ESC' untuk keluar dari program
    if cv2.waitKey(40) == 27:
        break

# Bersihkan memori setelah selesai
cap.release()
cv2.destroyAllWindows()
