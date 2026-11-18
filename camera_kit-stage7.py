# === Stage 7: Связи между сущностями ===
# Project: CameraKit
from datetime import date


class Item:
    def __init__(self, name, type, serial_number, purchase_date):
        self.name = name
        self.type = type
        self.serial_number = serial_number
        self.purchase_date = purchase_date

    def __repr__(self):
        return f"Item(name={self.name!r}, type={self.type!r}, serial_number={self.serial_number!r}, purchase_date={self.purchase_date!r})"


class Shot:
    def __init__(self, item, timestamp, settings):
        self.item = item
        self.timestamp = timestamp
        self.settings = settings

    def __repr__(self):
        return f"Shot(item={self.item!r}, timestamp={self.timestamp!r}, settings={self.settings!r})"


class CameraKit:
    def __init__(self):
        self.items = []
        self.shots = []

    def add_item(self, item):
        self.items.append(item)

    def add_shot(self, shot):
        self.shots.append(shot)

    def get_shots_by_item(self, item):
        return [shot for shot in self.shots if shot.item is item]

    def check_integrity(self, item):
        item_id = id(item)
        expected_shots = [shot for shot in self.shots if id(shot.item) == item_id]
        if len(expected_shots) != 0:
            return True
        return False


def main():
    kit = CameraKit()
    item = Item("Nikon D850", "camera", "1234567", date(2020, 1, 1))
    kit.add_item(item)
    kit.add_shot(Shot(item, date(2021, 5, 15), {"iso": 100, "aperture": 2.8}))
    kit.add_shot(Shot(item, date(2022, 3, 20), {"iso": 200, "aperture": 4.0}))
    kit.add_shot(Shot(Item("Canon EOS R5", "camera", "7654321", date(2021, 6, 1)), date(2023, 1, 1), {"iso": 400, "aperture": 5.6}))
    print(kit.get_shots_by_item(item))
    print(kit.check_integrity(item))


if __name__ == "__main__":
    main()
