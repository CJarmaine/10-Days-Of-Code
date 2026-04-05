from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "test.txt"


def parse_log_line(line: str) -> dict:
    ts_part, rest = line.split("]",1)
    timestamp = ts_part.strip("[]").strip()

    parts = [p.strip() for p in rest.split("|")]

    data = {"timestamp": timestamp}

    for part in parts:
        if part.startswith("Circuit:"):
            data["circuit_id"] = part.split(":", 1)[1].strip()
        elif part.startswith("Voltage:"):
            val_str = part.split(":", 1)[1].strip().rstrip("V").strip()
            data["voltage"] = float(val_str)
        elif part.startswith("Resistance:"):
            val_str = part.split(":", 1)[1].strip().rstrip("Ω").strip()
            data["resistance"] = float(val_str)
    return data


def collect_test_input() -> dict:
    circuit_id = input("Enter circuit ID: ")
    voltage_str = input("Enter Voltage (V): ")
    resistance_str = input("Enter resistance (Ω): ")

    test = {
        "circuit_id": circuit_id,
        "voltage": float(voltage_str),
        "resistance": float(resistance_str),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    return test

def read_tests() -> list[dict]:
    tests = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tests.append(parse_log_line(line))
    return tests

results = read_tests()
for test in results:
    print(test)

if __name__ == "__main__":
    test = collect_test_input()
    for key, value in test.items():
        print(f"{key}: {value}")