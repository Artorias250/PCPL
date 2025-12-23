class Library:
    def __init__(self, id, name, lang_id):
        self.id = id
        self.name = name
        self.lang_id = lang_id


class Language:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class LibraryLanguage:
    def __init__(self, lib_id, lang_id):
        self.lib_id = lib_id
        self.lang_id = lang_id


class ProgrammingData:
    def __init__(self):
        self.langs = [
            Language(1, "JavaScript"),
            Language(2, "Python"),
            Language(3, "TypeScript"),
        ]

        self.libs = [
            Library(1, "React", 1),
            Library(2, "Vue", 1),
            Library(3, "NumPy", 2),
            Library(4, "Django", 2),
            Library(5, "NestJS", 3),
        ]

        self.libs_langs = [
            LibraryLanguage(1, 1),
            LibraryLanguage(1, 3),
            LibraryLanguage(2, 1),
            LibraryLanguage(3, 2),
            LibraryLanguage(4, 2),
            LibraryLanguage(5, 3),
            LibraryLanguage(5, 1),
        ]

    def get_one_to_many(self):
        """Создает связь один-ко-многим"""
        return [(lib.name, lang.title)
                for lang in self.langs
                for lib in self.libs
                if lib.lang_id == lang.id]

    def get_many_to_many(self):
        """Создает связь многие-ко-многим"""
        many_to_many_temp = [(ll.lib_id, ll.lang_id) for ll in self.libs_langs]
        return [(lib.name, lang.title)
                for lib_id, lang_id in many_to_many_temp
                for lib in self.libs if lib.id == lib_id
                for lang in self.langs if lang.id == lang_id]


def func1(one_to_many):
    """Сортирует библиотеки по названию языка программирования"""
    return sorted(one_to_many, key=lambda x: x[1])


def func2(one_to_many, langs):
    """Сортирует языки по количеству библиотек"""
    res_b2_unsorted = []
    for lang in langs:
        libs_count = len([x for x in one_to_many if x[1] == lang.title])
        if libs_count > 0:
            res_b2_unsorted.append((lang.title, libs_count))
    return sorted(res_b2_unsorted, key=lambda x: x[1], reverse=True)


def func3(many_to_many):
    """Находит библиотеки, оканчивающиеся на 'JS'"""
    return [(lib_name, lang_title)
            for lib_name, lang_title in many_to_many
            if lib_name.endswith("JS")]


def main():
    data = ProgrammingData()
    one_to_many = data.get_one_to_many()
    many_to_many = data.get_many_to_many()

    print("Задание Б1: Отсортировать библиотеки по названию языка программирования")
    for lib in func1(one_to_many):
        print(f"  {lib[0]} - {lib[1]}")

    print("\nЗадание Б2: Отсортировать языки по количеству библиотек")
    for lang, count in func2(one_to_many, data.langs):
        print(f"  {lang}: {count} ")

    print("\nЗадание Б3: Найти библиотеки, оканчивающиеся на 'JS'")
    js_libs = func3(many_to_many)
    for lib_name, lang_title in js_libs:
        print(f"  {lib_name} - {lang_title}")


if __name__ == '__main__':
    main()
