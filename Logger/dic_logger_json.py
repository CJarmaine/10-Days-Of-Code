import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = BASE_DIR / "tests.json"


def collect_test_input():
    circuit_id = input("Enter circuit ID: ")
    voltage_str = input("Enter Voltage (V): ")
    resistance_str = input("Enter resistance (Ω): ")
    return {
        "circuit_id": circuit_id,
        "voltage": float(voltage_str),
        "resistance": float(resistance_str),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
   

def save_test(test):
    tests = []
    if FILE.exists():
        with open(FILE, "r", encoding="utf-8") as f:
            tests = json.load(f)
    tests.append(test)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tests, f, indent=4)

def read_tests():
    if not FILE.exists():
        print("No tests file yet")
        return
    with open(FILE, "r", encoding="utf-8") as f:
        tests = json.load(f)
    print(json.dumps(tests, indent=4))

if __name__ == "__main__":
    test = collect_test_input()
    save_test(test)
    read_tests()