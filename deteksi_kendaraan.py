import cv2
import numpy as np

# 1. Buka video lalu lintas
cap = cv2.VideoCapture('traffic.mp4')

# Baca 2 frame pertama untuk dibandingkan
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Status pause
is_paused = False

print("Program berjalan!")
print("Tekan 'SPASI' untuk Pause/Resume video.")
print("Tekan 'ESC' untuk Keluar.")

while cap.isOpened():
    # Jika video habis, kita loop (ulang dari awal)
    if not ret or frame2 is None:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        continue
        
    if not is_paused:
        # =========================================================================
        # TAHAP 1: IMAGE SUBTRACTING (Sesuai Materi Slide 03)
        # =========================================================================
        diff = cv2.absdiff(frame1, frame2)
        
        # =========================================================================
        # TAHAP 2: PENGOLAHAN CITRA BERWARNA (Sesuai Materi Slide 05)
        # =========================================================================
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        
        # =========================================================================
        # TAHAP 3: SPATIAL FILTERING & HISTOGRAM (Sesuai Materi Slide 04)
        # =========================================================================
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        
        # =========================================================================
        # TAHAP 4: MORFOLOGI CITRA (Sesuai Materi Slide 06)
        # =========================================================================
        dilated = cv2.dilate(thresh, None, iterations=3)
        
        # =========================================================================
        # TAHAP 5: PENGGAMBARAN KOTAK (Bounding Box)
        # =========================================================================
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output_frame = frame1.copy()

        for contour in contours:
            # Jika ukuran terlalu kecil, abaikan
            if cv2.contourArea(contour) < 700:
                continue
                
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(output_frame, "Kendaraan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # =========================================================================
        # TAHAP 6: GABUNGKAN 3 VIDEO MENJADI 1 JENDELA (Agar tidak tumpang tindih)
        # =========================================================================
        # Ubah gambar hitam putih menjadi format BGR agar bisa digabung dengan gambar asli
        thresh_bgr = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        dilated_bgr = cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)
        
        # Atur ukuran (resize) masing-masing menjadi 400x300 agar muat di layar laptop
        thresh_resized = cv2.resize(thresh_bgr, (400, 300))
        dilated_resized = cv2.resize(dilated_bgr, (400, 300))
        output_resized = cv2.resize(output_frame, (400, 300))
        
        # Berikan teks judul di pojok kiri atas tiap video
        cv2.putText(thresh_resized, "1. Threshold (Slide 04)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(dilated_resized, "2. Morfologi (Slide 06)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(output_resized, "3. Hasil Deteksi", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Gabungkan secara horizontal (berjejer ke samping)
        combined_video = np.hstack((thresh_resized, dilated_resized, output_resized))
        
        cv2.imshow("PCD - Deteksi Kendaraan (Tekan SPASI untuk Pause)", combined_video)
        
        # Lanjut ke frame berikutnya
        frame1 = frame2
        ret, frame2 = cap.read()

    # Tangkap tombol yang ditekan keyboard
    key = cv2.waitKey(40) & 0xFF
    
    if key == 27: # 27 adalah kode tombol ESC
        break
    elif key == ord(' '): # Tombol SPASI untuk Pause/Resume
        is_paused = not is_paused

cap.release()
cv2.destroyAllWindows()
