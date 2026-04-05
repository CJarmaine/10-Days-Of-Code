from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "test.txt"

def log_test():
    circuit_id = input("Circuit ID: ")
    voltage = input("Voltage (V): ")
    continuity = input("Continuity/Resistance (Ω)")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] Circuit: {circuit_id} | Voltage: {voltage}V | Resistance: {continuity} Ω \n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Test logged to: {LOG_FILE}")

def read_tests():
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())    

read_tests()
