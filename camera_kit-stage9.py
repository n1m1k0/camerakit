# === Stage 9: Сортировка записей ===
# Project: CameraKit
import datetime


def sort_by_name(records, reverse=False):
    return sorted(records, key=lambda record: record["name"], reverse=reverse)


def sort_by_created(records, reverse=False):
    return sorted(
        records,
        key=lambda record: record.get("created", datetime.datetime.min),
        reverse=reverse,
    )


def sort_records(records, field="name", reverse=False):
    if field == "name":
        return sort_by_name(records, reverse=reverse)
    if field == "created":
        return sort_by_created(records, reverse=reverse)
    raise ValueError("unknown field: " + field)
