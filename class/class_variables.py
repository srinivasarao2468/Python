class Employee:
    amount_increment=1.04
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname+"."+lname+"@gamil.com"
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def amount_rise(self):
        increment=self.salary*self.amount_increment
        return increment

emp1 = Employee("Sri", "alluri", 50000)
emp2 = Employee("Hari", "kammana", 60000)

#amount increment of all the class and instances are same
print(emp1.amount_increment)
print(emp2.amount_increment)
print(Employee.amount_increment)
print(emp1.amount_rise())

#increment ammount only for perticular
emp1.amount_increment=1.05
print(emp1.amount_increment)
print(emp2.amount_increment)
print(Employee.amount_increment)

#increment to class variable again it changes all the values of instances
Employee.amount_increment=1.06
print(emp1.__dict__)
print(emp1.amount_increment)
print(emp2.amount_increment)
print(Employee.amount_increment)
