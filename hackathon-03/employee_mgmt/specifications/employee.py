import uuid

class Employee:
    def __init__(self, name, department, designation, gross_salary, tax, bonus, employee_id=None):
        self.employee_id = employee_id or str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        #Employee.net_sal(self,self.tax,self.bonus, self.gross_salary)
        self.net_salary = Employee.net_sal(self, self.tax, self.bonus, self.gross_salary) #is this the right thing to do :) ?
        #self.net_salary = net_sal(self.tax,self.bonus, self.gross_salary)
        
    #@staticmethod
    def net_sal(self, tax, bonus, gross_salary):
        self.net_salary = self.gross_salary - (self.gross_salary * self.tax / 100) + self.bonus
        return self.net_salary
        #net_salary = gross_salary - (gross_salary * tax / 100) + bonus
        #return net_salary

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            employee_id = data["employee_id"],
            name = data["name"],
            department = data["department"],
            designation = data["designation"],
            gross_salary = data["gross_salary"],
            tax = data["tax"],
            bonus = data["bonus"]
            #net_salary = data["net_salary"]
        )