import numpy as np
from collections import Counter

def process_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Mengekstrak nilai waktu dari setiap baris
    time_differences = np.array([float(line.split()[2]) for line in lines])
    
    return time_differences

def detect_bot_interaction(data):
    # Mencari kemunculan data yang sama lebih dari 5 kali
    data_counter = Counter(data)
    for key, value in data_counter.items():
        if value > 2:
            return True

    # Mendeteksi pola sederhana (barisan atau deret)
    if is_arithmetic_sequence(data) or is_geometric_sequence(data):
        return True

    return False

def is_arithmetic_sequence(data):
    # Cek apakah data membentuk barisan aritmatika
    if len(data) < 3:
        return False
    
    diff = data[1] - data[0]
    for i in range(2, len(data)):
        if data[i] - data[i-1] != diff:
            return False
    return True

def is_geometric_sequence(data):
    # Cek apakah data membentuk barisan geometrik
    if len(data) < 3:
        return False
    
    ratio = data[1] / data[0]
    for i in range(2, len(data)):
        if data[i] / data[i-1] != ratio:
            return False
    return True