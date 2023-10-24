from Employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """Unit test for employee class"""

    def setUp(self):
        self.employee1 = Employee("Fred","Cob",54000)

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 59000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(6000)
        self.assertEqual(self.employee1.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()