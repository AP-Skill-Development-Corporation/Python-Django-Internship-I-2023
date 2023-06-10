r = 25
class Student:
    stid = "RT56"
    
    def stdinfo(self):
        print(f"Student Id: {self.stid}")

class Employee(Student):
    empid = "EM23"
    
    def empinfo(self):
        print(f"Employee id is: {self.empid}")


class Person(Employee):
    address = "Gntr"
    
    def person(self):
            print(f"Person address is: {self.address}")