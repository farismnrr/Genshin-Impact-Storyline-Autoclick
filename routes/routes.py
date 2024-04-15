import keyboard
import time
from controller.controller import run_bot_detection, run_perform_click

# Fungsi untuk menjalankan rute
def run_routes():
    # Loop sampai user menekan tombol 'space'
    print("Tekan 'space' untuk memulai program.")
    while True:
        if keyboard.is_pressed('space'):
            print("Memulai program...")
            run_perform_click()
            run_bot_detection()
            break
        time.sleep(0.1)
