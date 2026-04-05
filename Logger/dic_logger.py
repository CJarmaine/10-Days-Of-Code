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
            data["circuit_is"] = part.split(":", 1)[1].strip()
        elif part.startswith("Voltage:"):
            val_str = part.split(":", 1)[1].strip().rstrip("V").strip()
            data["voltage"] = float(val_str)
        elif part.startswith("Resistance:"):
            val_str = part.split(":", 1)[1].strip().rstrip("Ω").strip()
            data["resistance"] = float(val_str)
    return data

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