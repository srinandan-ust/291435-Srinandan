import json
class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        #print("Parent class details:" , self.name, self.age, self.gender)

    def get_details(self):
        return ','.join([str(self.name), str(self.age), str(self.gender)])

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        #print("Subclass Details:" , self.name, self.age, self.gender, self.emp_id, self.department, self.salary)

    def get_details(self):
        return super().get_details() + f", Emp ID: " + str(self.emp_id) + ", Department: " + self.department + ", Salary: " + str(self.salary)

    def is_eligible_for_bonus(self):
        if (self.salary < 50000):
            return True

        else:
            return False


    def from_string(cls, data_string):
        name, age, gender, emp_id, dep, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, dep, float(salary))
    
    from_string = classmethod(from_string)

    def bonus_policy():
        print("Eligible for bonus only if salary is less than 50000")
        
    bonus_policy = staticmethod(bonus_policy)

class Department:
    def __init__(self, name):
        self.name = name
        self.employeelist = []

    def add_employee(self, employee):
        self.employeelist.append(employee)

    def get_average_salary(self):
        if not self.employeelist:
            pass
        total_salary = sum(emp.salary for emp in self.employeelist)
        return total_salary / len(self.employeelist)

    def get_all_employees(self):
        return self.employeelist

def save_to_json(employees, filename="employees.json"):
    data = []
    for emp in employees:
        data.append({"name": emp.name, "age": emp.age, "gender": emp.gender, "emp_id": emp.emp_id, "department": emp.department, "salary": emp.salary})
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
 
def load_from_json(filename="employees.json"):
    with open(filename, 'r') as f2:
        data = json.load(f2)
    employees = []
    for emp_data in data:
        emp = Employee(name=emp_data['name'], age=emp_data['age'], gender=emp_data['gender'], emp_id=emp_data['emp_id'], department=emp_data['department'], salary=emp_data['salary'])
        employees.append(emp)
    return employees