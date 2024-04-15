import keyboard
import random
import os
import time

# Persentase kemunculan untuk setiap interval
interval_percentage = {
    "Interval 1": 15,
    "Interval 2": 40,
    "Interval 3": 45
}

# Fungsi untuk menekan tombol "space"
def press_button():
    keyboard.press("space")

# Fungsi untuk memilih interval berdasarkan persentase
def choose_interval():
    rand_num = random.randint(1, 100)
    cumulative_percentage = 0
    for interval, percentage in interval_percentage.items():
        cumulative_percentage += percentage
        if rand_num <= cumulative_percentage:
            return interval

# Fungsi untuk menghasilkan waktu tunggu antara tekanan tombol "space"
def generate_wait_time(interval):
    if interval == "Interval 1":
        interval_time = random.randint(1000, 1500)  # Update rentang waktu interval (ms)
    elif interval == "Interval 2":
        interval_time = random.randint(500, 1000)    # Update rentang waktu interval (ms)
    else:
        interval_time = random.randint(100, 500)     # Update rentang waktu interval (ms)
    return interval_time  # Mengembalikan waktu interval dalam milidetik (ms)

# Fungsi untuk menulis nilai time_difference_ms ke file output.txt
def write_time_difference_to_file(time_difference_ms):
    output_file_path = get_output_file_path()
    with open(output_file_path, 'a') as file:
        file.write(f'Time Difference: {time_difference_ms:.2f} ms\n')

# Fungsi untuk menghapus isi file output.txt
def clear_output_file():
    output_file_path = get_output_file_path()
    with open(output_file_path, 'w') as file:
        pass

# Fungsi untuk mendapatkan path file output.txt
def get_output_file_path():
    # Dapatkan path dari folder saat ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Dapatkan path ke folder satu level di atas folder saat ini
    parent_dir = os.path.dirname(current_dir)
    # Gabungkan path folder dengan nama file output.txt
    return os.path.join(parent_dir, 'output.txt')

# Fungsi untuk melakukan klik
def perform_click():
    interval = choose_interval()  # Pilih interval
    press_button()
    time.sleep(generate_wait_time(interval) / 1000)  # Mengubah waktu interval ke detik (ms -> detik)
    return interval