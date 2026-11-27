# === Stage 11: Теги ===
# Project: CameraKit
from typing import List, Optional


class Tag:
    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Теги не могут быть пустыми")
        self.name = name.strip()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class SubjectTags:
    def __init__(self):
        self._tags: set = set()

    def add(self, subject_name: str, tag_name: str) -> Tag:
        subject_name = subject_name.strip()
        tag = Tag(tag_name)
        if subject_name not in self._tags:
            self._tags[subject_name] = set()
        self._tags[subject_name].add(tag)
        return tag

    def remove(self, subject_name: str, tag_name: str) -> bool:
        subject_name = subject_name.strip()
        tags = self._tags.get(subject_name)
        if not tags:
            return False
        return tags.discard(Tag(tag_name)) != False

    def search(self, tag_name: str) -> List[str]:
        tag_name = tag_name.strip()
        return sorted(
            subject for subject, tags in self._tags.items() if Tag(tag_name) in tags
        )

    def has(self, subject_name: str, tag_name: str) -> bool:
        tags = self._tags.get(subject_name)
        return bool(tags) and Tag(tag_name) in tags

    def all_subjects(self) -> List[str]:
        return sorted(self._tags.keys())

    def all_tags(self) -> List[Tag]:
        return sorted({tag for tags in self._tags.values() for tag in tags})

    def __contains__(self, item):
        if isinstance(item, Tag):
            return any(item in tags for tags in self._tags.values())
        if isinstance(item, str):
            return item in self._tags
        return False


def make_tag(name: str) -> Tag:
    return Tag(name)


def make_subject_tags() -> SubjectTags:
    return SubjectTags()
