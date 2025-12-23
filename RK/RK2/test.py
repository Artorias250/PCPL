import unittest
from main import ProgrammingData, func1, func2, func3


class TestProgrammingData(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.data = ProgrammingData()
        self.one_to_many = self.data.get_one_to_many()
        self.many_to_many = self.data.get_many_to_many()

    def test_func1_sort_libraries_by_language(self):
        """Тест 1: Проверка сортировки библиотек по языку программирования"""
        sorted_libs = func1(self.one_to_many)
        languages = [lang for _, lang in sorted_libs]
        self.assertEqual(languages, sorted(languages))
        expected_first = ("React", "JavaScript")
        expected_last = ("NestJS", "TypeScript")
        self.assertEqual(sorted_libs[0], expected_first)
        self.assertEqual(sorted_libs[-1], expected_last)
        self.assertEqual(len(sorted_libs), len(self.one_to_many))

    def test_func2_count_libraries_per_language(self):
        """Тест 2: Проверка подсчета библиотек для каждого языка"""
        lang_counts = func2(self.one_to_many, self.data.langs)
        counts = [count for _, count in lang_counts]
        self.assertEqual(counts, sorted(counts, reverse=True))
        expected_counts = [
            ("JavaScript", 2),
            ("Python", 2),
            ("TypeScript", 1),
        ]
        self.assertEqual(lang_counts, expected_counts)

        language_names = [lang for lang, _ in lang_counts]
        self.assertIn("JavaScript", language_names)
        self.assertIn("Python", language_names)
        self.assertIn("TypeScript", language_names)

    def test_func3_find_js_libraries(self):
        """Тест 3: Поиск библиотек, оканчивающихся на 'JS'"""

        js_libs = func3(self.many_to_many)

        for lib_name, _ in js_libs:
            self.assertTrue(lib_name.endswith('JS'))

        expected_libs = [("NestJS", "TypeScript"), ("NestJS", "JavaScript")]
        self.assertEqual(len(js_libs), len(expected_libs))

        for expected in expected_libs:
            self.assertIn(expected, js_libs)

        non_js_libs = [("Vue", "JavaScript"), ("NumPy", "Python"), ("Django", "Python")]
        for non_js in non_js_libs:
            self.assertNotIn(non_js, js_libs)

    def test_programming_data_structure(self):
        """Дополнительный тест: Проверка структуры данных"""
        self.assertEqual(len(self.data.langs), 3)
        self.assertEqual(len(self.data.libs), 5)
        self.assertEqual(len(self.data.libs_langs), 7)
        self.assertEqual(len(self.one_to_many), 5)
        self.assertEqual(len(self.many_to_many), 7)


if __name__ == '__main__':
    unittest.main()
