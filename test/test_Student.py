import unittest
from class_definitions import Student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Shannon', 'Aidan', 'English')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "Aidan")
        self.assertEqual(self.student.last_name, "Shannon")
        self.assertEqual(self.student.major, "English")
        self.assertEqual(self.student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        student = t.Student("Shannon", "Aidan", "CompSci", 4.0)
        assert student.last_name == "Shannon"
        assert student.first_name == "Aidan"
        assert student.major == "CompSci"
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Shannon, Aidan has major English with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student("1234asfas", "Aidan", "English", 4.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Shannon", "1234asfas", "English", 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Potter", "Harry", "Spell", 4.0)

    def test_object_not_created_error_gpa_high(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Potter", "Harry", "Necromancy", 4.5)

    def test_object_not_created_error_gpa_low(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Potter", "Harry", "Necromancy", -4.5)

    def test_object_not_created_error_gpa_not_float(self):
        with self.assertRaises(ValueError):
            stu = t.Student("Potter", "Harry", "Necromancy", 'A')


if __name__ == '__main__':
    unittest.main()
