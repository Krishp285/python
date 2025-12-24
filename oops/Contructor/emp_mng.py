# Employee Management System
# add , delete , update , search , display employee details

class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.list_of_employees = []

    def add_employee(self):
        self.emp_id = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.age = input("Enter Employee Age: ")
        self.department = input("Enter Employee Department: ")

        self.save_employee()

    def save_employee(self):
        employee = {
            "ID": self.emp_id,
            "Name": self.name,
            "Age": self.age,
            "Department": self.department
        }
        self.list_of_employees.append(employee)
        print("Employee added successfully.")


    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Department: {self.department}")

    def display_all_employees(self):
        for emp in self.list_of_employees:
            print(emp)
      
    def search_employee(self, name):
        for emp in self.list_of_employees:
            if emp["Name"] == name:
                print("Employee found:")
                print(emp)
                return
        print("Employee not found.")

    def delete_employee(self, emp_id):
        for emp in self.list_of_employees:
            if emp["ID"] == emp_id:
                self.list_of_employees.remove(emp)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

    
    def update_employee(self, emp_id):
        for emp in self.list_of_employees:
            if emp["ID"] == emp_id:
                emp["Name"] = input("Enter new name: ")
                emp["Age"] = input("Enter new age: ")
                emp["Department"] = input("Enter new department: ")
                print("Employee updated successfully.")
                return
        print("Employee not found.")

emp_mng = Employee(None, None, None, None)

while True:
    print("Employee Management System")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Update Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            emp_mng.add_employee()
        case 2:
            emp_mng.display_all_employees()
        case 3:
            name = input("Enter Employee Name to search: ")
            emp_mng.search_employee(name)
        case 4:
            emp_id = input("Enter Employee ID to delete: ")
            emp_mng.delete_employee(emp_id)
        case 5:
            emp_id = input("Enter Employee ID to update: ")
            emp_mng.update_employee(emp_id)
        case 6:
            print("Exiting the system.")
        case _:
            print("Invalid choice.")
