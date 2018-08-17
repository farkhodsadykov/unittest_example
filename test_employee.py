import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Simple a Class TestEmployee"""

    def test_email(self):
        """Method test_email check's method email in Employee Object"""

        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        self.assertEqual(emp_1.email, 'corey.schafer@evolvecyber.com')
        self.assertEqual(emp_2.email, 'sue.smith@evolvecyber.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
        self.assertEqual(emp_1.email, 'john.schafer@evolvecyber.com')
        self.assertEqual(emp_2.email, 'jane.smith@evolvecyber.com')



    def test_fullname(self):
        """Method test_fullname check's method fullname in Employee Object"""

        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

if __name__ == '__main__':
    unittest.main()
