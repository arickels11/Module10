import unittest
from student_class import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.stud = Student('Rickels', 'Alex', 'Econ')

    def tearDown(self):
        del self.stud

    def test_object_created_required_attributes(self):
        self.assertEqual(self.stud.last_name, 'Rickels')
        self.assertEqual(self.stud.first_name, 'Alex')
        self.assertEqual(self.stud.major, 'Econ')
        self.assertEqual(self.stud.gpa, 0.0)

    def test_object_created_all_attributes(self):
        studenta = Student('Rickels', 'Alex', 'Econ', 4.0)
        assert studenta.last_name == 'Rickels'
        assert studenta.first_name == 'Alex'
        assert studenta.major == 'Econ'
        assert studenta.gpa == 4.0


















if __name__ == '__main__':
    unittest.main()
