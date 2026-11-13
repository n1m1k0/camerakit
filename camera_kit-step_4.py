# === Stage 4: Редактирование записей ===
# Project: CameraKit
from datetime import date


def _validate_field(value, field):
    if field == "name":
        if not isinstance(value, str) or not value.strip():
            return False
        return True
    if field == "type":
        allowed = {"camera", "lens", "shutter"}
        return value in allowed
    if field == "serial_number":
        if not isinstance(value, str) or not value.strip():
            return False
        return True
    if field == "purchase_date":
        if not isinstance(value, date):
            return False
        return True
    return False


def _build_update_payload(fields):
    payload = {}
    for field, value in fields.items():
        if _validate_field(value, field):
            payload[field] = value
    return payload


def edit_subject(subject_id, fields):
    if not isinstance(subject_id, int) or subject_id <= 0:
        return None
    if not isinstance(fields, dict):
        return None

    valid_fields = {"name", "type", "serial_number", "purchase_date"}
    provided = set(fields.keys()) & valid_fields
    if not provided:
        return None

    valid = _build_update_payload(fields)
    if not valid:
        return None

    return valid
