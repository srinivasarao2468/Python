class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname+"."+lname+"@gamil.com"
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def amount_rise(self):
        amount_increment=1.04
        increment=self.salary*amount_increment
        return increment

emp1 = Employee("Sri", "alluri", 50000)
emp2 = Employee("Hari", "kammana", 60000)

print(emp1.fullname())
print(emp2.fullname())
print(emp1.amount_rise())
print(emp2.amount_rise())
