# === Stage 8: Фильтрация записей ===
# Project: CameraKit
def filter_items_by_type(items, item_type):
    """Фильтрует предметы по значению поля 'тип'."""
    return [item for item in items if item.get("тип") == item_type]


def filter_items_by_date_range(items, start_date, end_date):
    """Фильтрует предметы по диапазону дат покупки (включительно)."""
    if start_date is None:
        start_date = float("-inf")
    if end_date is None:
        end_date = float("inf")
    return [item for item in items if start_date <= item.get("дата покупки") <= end_date]


def filter_items_by_any(items, *, item_type=None, start_date=None, end_date=None):
    """
    Комбинирует фильтрацию по типу и диапазону дат.
    Передаются только те фильтры, которые нужны (остальные None).
    """
    filtered = items
    if item_type is not None:
        filtered = filter_items_by_type(filtered, item_type)
    if start_date is not None or end_date is not None:
        filtered = filter_items_by_date_range(filtered, start_date, end_date)
    return filtered


def find_items_by_serial(items, serial_number):
    """Возвращает предметы с совпадающим серийным номером (все вхождения)."""
    return [item for item in items if item.get("серийный номер") == serial_number]


def group_items_by_type(items):
    """Группирует предметы по полю 'тип' и возвращает словарь тип -> список."""
    grouped = {}
    for item in items:
        grouped.setdefault(item.get("тип"), []).append(item)
    return grouped


def summarize_items(items):
    """Возвращает подсчёт: общее число, уникальные типы и дубликаты по серийному номеру."""
    total = len(items)
    types = {item.get("тип") for item in items}
    serials = {}
    for item in items:
        serials[item.get("серийный номер")] = serials.get(item.get("серийный номер"), 0) + 1
    duplicated = {serial: count for serial, count in serials.items() if count > 1}
    return {"total": total, "types": types, "duplicated_serials": duplicated}
