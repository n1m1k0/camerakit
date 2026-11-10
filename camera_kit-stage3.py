# === Stage 3: Хранилище в памяти ===
# Project: CameraKit
import uuid
from datetime import date


class Item:
    def __init__(self, name, item_type, serial_number, purchase_date):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = item_type
        self.serial_number = serial_number
        self.purchase_date = purchase_date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "serial_number": self.serial_number,
            "purchase_date": self.purchase_date.isoformat() if isinstance(self.purchase_date, date) else self.purchase_date,
        }

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name!r}, type={self.type!r}, serial_number={self.serial_number!r}, purchase_date={self.purchase_date!r})"


class ItemStore:
    def __init__(self):
        self._items = {}

    def add(self, item):
        self._items[item.id] = item
        return item

    def get(self, item_id):
        return self._items.get(item_id)

    def list_items(self):
        return list(self._items.values())
