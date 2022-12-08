from django.test import TestCase
from students.models import Student


class TestStudent(TestCase):
    def test_short_str(self):
        s = Student()
        s.last_name = "Сидоров"
        s.first_name = "Сидор"
        s.number = "1234"
        res = str(s)
        self.assertEqual(res, "Сидоров С.")

    def test_long_str(self):
        s = Student()
        s.last_name = "Сидоров"
        s.first_name = "Сидор"
        s.second_name = "Сидорович"
        s.number = "1234"
        res = str(s)
        self.assertEqual(res, "Сидоров С.С.")
