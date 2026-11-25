# === Stage 10: Поиск по нескольким словам ===
# Project: CameraKit
def parse_search_query(query):
    """
    Разбирает поисковый запрос в набор включений и исключений.

    Включаются слова, которые должны присутствовать в названии.
    Исключаются слова, имеющие префикс «-» — они должны отсутствовать.

    Возвращает кортеж (include_terms, exclude_terms).
    """
    include_terms = []
    exclude_terms = []

    for word in query.split():
        if word.startswith('-'):
            exclude_terms.append(word[1:].strip().lower())
        else:
            include_terms.append(word.strip().lower())

    return include_terms, exclude_terms


def matches_query(item_name, include_terms, exclude_terms):
    """
    Проверяет, соответствует ли название предмета поисковому запросу.

    Все включающие слова должны встречаться в названии (без учёта регистра).
    Ни одно из исключающих слов не должно встречаться в названии.

    Возвращает True при совпадении, иначе False.
    """
    name = item_name.lower()

    for term in include_terms:
        if term not in name:
            return False

    for term in exclude_terms:
        if term in name:
            return False

    return True


class SearchBuilder:
    """
    Построитель поиска предметов по нескольким словам с поддержкой исключений.

    Метод add_term добавляет включающий термин.
    Метод exclude_term добавляет исключающий термин (с префиксом «-»).
    Метод build собирает финальный запрос и применяет его к коллекции.
    """

    def __init__(self):
        self.include_terms = []
        self.exclude_terms = []

    def add_term(self, term):
        self.include_terms.append(term.strip().lower())
        return self

    def exclude_term(self, term):
        self.exclude_terms.append(term.strip().lower())
        return self

    def build(self, items):
        result = []
        for item in items:
            if matches_query(item.get('name', ''), self.include_terms, self.exclude_terms):
                result.append(item)
        return result


def search_items(items, query):
    """
    Удобен для прямого вызова.

    Разбирает строку запроса и возвращает список подходящих предметов.
    """
    include_terms, exclude_terms = parse_search_query(query)
    return [item for item in items if matches_query(item.get('name', ''), include_terms, exclude_terms)]


if __name__ == '__main__':
    items = [
        {'name': 'Canon EOS 5D Mark IV', 'type': 'camera'},
        {'name': 'Nikon Z5', 'type': 'camera'},
        {'name': 'Canon EF 50mm f/1.4', 'type': 'lens'},
        {'name': 'Sony 35mm', 'type': 'lens'},
        {'name': 'Canon EOS Rebel T7', 'type': 'camera'},
    ]

    print(search_items(items, 'canon'))
    print(search_items(items, 'canon -sony'))
