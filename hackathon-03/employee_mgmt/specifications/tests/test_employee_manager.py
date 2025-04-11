import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        emp = self.manager.add_employee("Fernando", "Finance", "Assosciate", 4000, 5, 200)
        self.assertEqual(emp.name, "Fernando")
        self.assertEqual(emp.department, "Finance")
        self.assertEqual(emp.designation, "Assosciate")
        self.assertEqual(emp.gross_salary, 4000)
        self.assertEqual(emp.tax, 5)
        self.assertEqual(emp.bonus, 200)

    def test_get_all_employees(self):
        self.manager.add_employee("Karan Sanjeev", "Cloud infra", "Lead", 45000, 18, 1500)
        self.manager.add_employee("Benoy", "IT", "Executive", 42000, 6, 1000)
        employees = self.manager.get_all_employees()
        self.assertEqual(len(employees), 2)

    def test_find_employee_by_id(self):
        emp = self.manager.add_employee("Diana", "HR", "Manager", 190000, 7, 10000)
        found = self.manager.find_employee_by_id(emp.employee_id)
        self.assertEqual(found.name, "Diana")

    def test_find_employee_by_id_not_found(self):
        emp = self.manager.find_employee_by_id("non-existent-id")
        self.assertEqual(emp, None)

    def test_delete_employee(self):
        emp = self.manager.add_employee("Kumar Singh", "Automation", "Tester", 31000, 5, 800)
        deleted = self.manager.delete_employee(emp.employee_id)
        self.assertEqual(deleted, True)
        self.assertEqual(len(self.manager.get_all_employees()), 0)

    def test_delete_employee_not_found(self):
        deleted = self.manager.delete_employee("this id is just a dummy fake id for testing")
        self.assertEqual(deleted, False)

    def test_export_employees(self):
        self.manager.add_employee("Farhan", "HR", "Recruiter", 37000, 10, 1200)
        exported = self.manager.export_employees()
        self.assertEqual(len(exported), 1)
        self.assertEqual(exported[0]['name'], "Farhan")

    def test_load_employees(self):
        data = [{"employee_id": "test-id", "name": "Gautham Vasudev", "department": "Admininstration", "designation": "Senior Executive", "gross_salary": 13300, "tax": 15, "bonus": 4000}]
        self.manager.load_employees(data)
        loaded = self.manager.get_all_employees()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Gautham Vasudev")

if __name__ == '__main__':
    unittest.main()