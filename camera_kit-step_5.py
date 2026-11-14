# === Stage 5: Удаление и восстановление ===
# Project: CameraKit
import datetime


class SoftDeleted:
    """Базовый класс для сущности, поддерживающей мягкое удаление.

    Вместо физического удаления из хранилища объект помечается флагом
    deleted, что позволяет при необходимости вернуть его в активное
    состояние.
    """

    def __init__(self, name, item_type, serial, purchase_date):
        self.name = name
        self.item_type = item_type
        self.serial = serial
        self.purchase_date = purchase_date
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.datetime.now(datetime.timezone.utc)

    def restore(self):
        self.deleted = False
        self.deleted_at = None


class Subject(SoftDeleted):
    """Предмет учёта: камера, объектив, затвор и т. п.

    Сущность «предмет» с полями название, тип, серийный номер и дата
    покупки, расширяющая базовые возможности мягкого удаления.
    """

    def __init__(self, name, item_type, serial, purchase_date):
        super().__init__(name, item_type, serial, purchase_date)

    def __repr__(self):
        status = "активный" if not self.deleted else "удалён"
        return f"<Subject {self.name!r} ({status})>"


def remove_subject(subject):
    subject.soft_delete()
    return subject


def restore_subject(subject):
    if subject.deleted:
        subject.restore()
        return True
    return False


def list_active(subjects):
    return [s for s in subjects if not s.deleted]


def list_deleted(subjects):
    return [s for s in subjects if s.deleted]
