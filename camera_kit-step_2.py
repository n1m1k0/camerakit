# === Stage 2: Проверка полей ===
# Project: CameraKit
def normalize_text(value):
    if value is None:
        return ""
    return value.strip()


def normalize_serial(value):
    if value is None:
        return ""
    return value.strip().upper()


def normalize_date(value):
    if value is None:
        return ""
    return value.strip()


class FieldError(Exception):
    pass


def validate_name(name):
    if name is None or name.strip() == "":
        raise FieldError("Название не может быть пустым")
    if len(name.strip()) > 100:
        raise FieldError("Название слишком длинное (максимум 100 символов)")
    return name.strip()


def validate_type(item_type):
    if item_type is None or item_type.strip() == "":
        raise FieldError("Тип не может быть пустым")
    return item_type.strip()


def validate_serial(serial):
    if serial is None or serial.strip() == "":
        raise FieldError("Серийный номер не может быть пустым")
    if len(serial.strip()) > 50:
        raise FieldError("Серийный номер слишком длинный (максимум 50 символов)")
    return serial.strip().upper()


def validate_purchase_date(date_value):
    if date_value is None or date_value.strip() == "":
        raise FieldError("Дата покупки не может быть пустой")
    return date_value.strip()


def validate_item(name, item_type, serial, purchase_date):
    errors = []
    try:
        name = validate_name(name)
    except FieldError as exc:
        errors.append(str(exc))
    try:
        item_type = validate_type(item_type)
    except FieldError as exc:
        errors.append(str(exc))
    try:
        serial = validate_serial(serial)
    except FieldError as exc:
        errors.append(str(exc))
    try:
        purchase_date = validate_purchase_date(purchase_date)
    except FieldError as exc:
        errors.append(str(exc))
    if errors:
        raise FieldError("\n".join(errors))
    return name, item_type, serial, purchase_date
