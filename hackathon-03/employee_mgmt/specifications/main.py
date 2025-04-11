from employee_manager import EmployeeManager
import storage
 
def menu():
    print("\nEmployee Management System\n1. Add new Employee\n2. View All Employees\n3. Search Employee by EmployeeID\n4. Delete Employee\n5. Exit")
 
def main():
    manager = EmployeeManager()
    
    #data = storage.load_from_file()
    #manager.load_employees(data)
    
    store = storage.Storage()
    data = store.load()
    manager.load_employees(data)
    
    store.save(manager.export_employees())
    
    
    while True:
        menu()
        choice = input("Enter choice: ").strip()
 
        if choice == '1':
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")
            gross_salary = float(input("Gross salary: "))
            tax = float(input("Tax Percentage: "))
            bonus = float(input("Enter the Bonus: "))
            employee = manager.add_employee(name, department, designation, gross_salary, tax, bonus)
            print(f"Added!✓ -> ID of the employee is: {employee.employee_id}")
        elif choice == '2':
            for s in manager.get_all_employees():
                print(s.to_dict())
 
        elif choice == '3':
            sid = input("Enter the employee ID: ")
            employee = manager.find_employee_by_id(sid)
            print(employee.to_dict() if employee else "Employee details not found")
 
        elif choice == '4':
            sid = input("Enter the Employee ID to delete: ")
            if manager.delete_employee(sid):
                print("Deleted Employee details")
            else:
                print("No such Employee exists")
        elif choice == '5':
            store.save(manager.export_employees())
            print("Saved to file")
            break
        else:
            print("Invalid option ✗")
 
if __name__ == "__main__":
    main()