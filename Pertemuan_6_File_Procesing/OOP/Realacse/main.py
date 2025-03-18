from Manager import Manager
from Employee import Employee

def main():
    employee = Employee("Tika", 20 , "Software Enginer" , 10000000)
    manager = Manager("Bob",40, "Project manager" , 25000000, 10)
    
    employee.setUmur(22)
    print(employee.get_detail())
    print(employee.get_work())
    print(manager.get_detail())
    print(manager.get_work())

if __name__ == "__main__":
    main()