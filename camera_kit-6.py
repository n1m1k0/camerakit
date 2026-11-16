# === Stage 6: Связанная сущность ===
# Project: CameraKit
import datetime


class Subject:
    def __init__(self, name, type_name, serial_number, purchase_date):
        self.name = name
        self.type_name = type_name
        self.serial_number = serial_number
        self.purchase_date = purchase_date

    def __repr__(self):
        return f"Subject(name={self.name!r}, type_name={self.type_name!r}, serial_number={self.serial_number!r}, purchase_date={self.purchase_date!r})"


class Shooting:
    def __init__(self, subject_id, subject, description, date):
        self.id = subject_id
        self.subject = subject
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Shooting(id={self.id!r}, subject={self.subject!r}, description={self.description!r}, date={self.date!r})"


def add_shooting(shootings, subject_id, subject, description, date):
    shooting = Shooting(subject_id, subject, description, date)
    shootings.append(shooting)
    return shooting


if __name__ == "__main__":
    subjects = []
    shootings = []

    camera = Subject("Sony A7III", "camera", "SN123456", datetime.date(2020, 1, 15))
    subjects.append(camera)

    shooting = add_shooting(
        shootings,
        subjects[0].id,
        subjects[0],
        "Портрет на улице",
        datetime.date(2022, 6, 10),
    )

    print(shooting)
