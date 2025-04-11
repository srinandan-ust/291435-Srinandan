import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        emp = Employee("Hareesh", "Automotive", "Lead", 50000, 10, 5000)
        self.assertEqual(emp.name, "Hareesh")
        self.assertEqual(emp.department, "Automotive")
        self.assertEqual(emp.designation, "Lead")
        self.assertEqual(emp.gross_salary, 50000)
        self.assertEqual(emp.tax, 10)
        self.assertEqual(emp.bonus, 5000)
        expected_net = 50000 - (50000 * 10 / 100) + 5000
        self.assertEqual(emp.net_salary, expected_net)

    def test_to_dict(self):
        emp = Employee("Sree", "HR", "Assosciate", 40000, 15, 400)
        emp_dict = emp.to_dict()
        self.assertEqual(emp_dict["name"], "Sree")
        self.assertEqual(emp_dict["department"], "HR")
        self.assertEqual(emp_dict["designation"], "Assosciate")
        self.assertEqual(emp_dict["gross_salary"], 40000)
        self.assertEqual(emp_dict["tax"], 15)
        self.assertEqual(emp_dict["bonus"], 400)
        self.assertEqual(emp_dict["net_salary"], 40000 - (40000 * 15 / 100) + 400)

    def test_from_dict(self):
        data = {"employee_id": "acae-acdh-semicon", "name": "Nath Kumar", "department": "Medical Electronics", "designation": "Engineer", "gross_salary": 55000, "tax": 12, "bonus": 400}
        emp = Employee.from_dict(data)
        self.assertEqual(emp.employee_id, "acae-acdh-semicon")
        self.assertEqual(emp.name, "Nath Kumar")
        self.assertEqual(emp.department, "Medical Electronics")
        self.assertEqual(emp.designation, "Engineer")
        self.assertEqual(emp.gross_salary, 55000)
        self.assertEqual(emp.tax, 12)
        self.assertEqual(emp.bonus, 400)

if __name__ == '__main__':
    unittest.main()