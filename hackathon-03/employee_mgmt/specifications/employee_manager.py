from employee import Employee
 
class EmployeeManager:
    def __init__(self):
        self.employees = []
 
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee
 
    def get_all_employees(self):
        return self.employees
 
    def find_employee_by_id(self, employee_id):
        return next((s for s in self.employees if s.employee_id == employee_id), None)
 
    def delete_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False
 
    def load_employees(self, employee_list):
        self.employees = [Employee.from_dict(data) for data in employee_list]
 
    def export_employees(self):
        return [s.to_dict() for s in self.employees]