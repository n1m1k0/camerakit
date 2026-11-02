# === Stage 1: Каркас модуля ===
# Project: CameraKit
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Subject:
    name: str
    kind: str
    serial: str
    purchase_date: date


def make_demo_records() -> list[Subject]:
    return [
        Subject("Canon EOS R5", "camera", "CR5-2024-001", date(2024, 1, 15)),
        Subject("Sigma 24-70mm f/2.8", "lens", "LNS-2024-042", date(2024, 2, 3)),
        Subject("Canon EOS R5", "camera", "CR5-2024-001", date(2024, 1, 15)),
        Subject("Tamron 70-180mm f/2.8", "lens", "TMR-2024-019", date(2024, 3, 22)),
    ]


def main() -> None:
    records = make_demo_records()
    for record in records:
        print(f"{record.name} ({record.kind}, {record.serial}, куплено {record.purchase_date})")


if __name__ == "__main__":
    main()
