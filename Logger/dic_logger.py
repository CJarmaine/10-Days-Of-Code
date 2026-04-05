test = {
    "circuit_id": "C1",
    "voltage": 240,
    "resistance": 12.5,
    "timestamp": "2026-04-05 14:30"
}

print(test["voltage"])

test["status"] = "pass"

for key, value in test.items():
    print(f"{key}: {value}")