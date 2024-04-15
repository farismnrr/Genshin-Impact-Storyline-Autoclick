import time
import keyboard
import numpy as np
from sklearn.ensemble import IsolationForest
from helper.bot_detection_helper import process_data, detect_bot_interaction
from helper.click_helper import perform_click, clear_output_file, write_time_difference_to_file

# Fungsi utama untuk menjalankan perform click
def run_perform_click():
    clear_output_file()
    last_press_time = None
    click_num = 0

    while True:
        if keyboard.is_pressed('esc'):  # Cek apakah tombol 'esc' ditekan
            print("Program dihentikan.")
            break  # Keluar dari loop dan akhiri program
            
        click_num += 1
        interval = perform_click()
        
        current_time = time.time()
        if last_press_time is not None:
            time_difference_ms = (current_time - last_press_time) * 1000
            if time_difference_ms > 20:  # Hanya tampilkan jika jarak waktu di atas 20ms
                # print(f"Jarak waktu antar press: {time_difference_ms:.2f} ms")
                print(f"Klik ke-{click_num}, Interval yang dipilih: {interval}, Waktu Interval: {time_difference_ms:.2f} ms")
                # Panggil fungsi untuk menulis time_difference_ms ke dalam file
                write_time_difference_to_file(time_difference_ms)
        last_press_time = current_time

        time.sleep(0.1)  # Menambahkan sedikit jeda untuk mengurangi penggunaan CPU

def run_bot_detection():
    # Persiapan data
    X = process_data('output.txt')
    if detect_bot_interaction(X):
        print("Bot Interaction Detected")
        return
    
    # Pemilihan model dan pelatihan
    clf = IsolationForest()
    clf.fit(X.reshape(-1, 1))  # Perubahan disini
    
    # Prediksi anomali
    anomaly_predictions = clf.predict(X.reshape(-1, 1))  # Dan di sini
    
    # Menghitung jumlah anomali
    num_anomalies = np.sum(anomaly_predictions == -1)
    
    # Mencetak hasil deteksi
    bot_percentage = (num_anomalies / len(X)) * 100
    human_percentage = 100 - bot_percentage
    print(f"{human_percentage:.2f}% Human Interaction")
    print(f"{bot_percentage:.2f}% Bot Interaction")
