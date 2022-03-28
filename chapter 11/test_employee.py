import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee("ana", "barros", 500)

    def test_give_default_raise(self):
        self.default_raise = self.new_employee.give_raise()
        self.assertEqual(self.default_raise, 5500)

    def test_give_custom_raise(self):
        self.custom_raise = self.new_employee.give_raise(100)
        self.assertEqual(self.custom_raise, 600)


if __name__ == "__main__":
    unittest.main()
