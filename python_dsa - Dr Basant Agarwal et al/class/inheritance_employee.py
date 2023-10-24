class Employee():
    numEmployee = 0

    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate 
        Employee.numEmployee += 1
    
    def __del__ (self):
        Employee.numEmployee -= 1
    
    def hours(self, numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return ("payed %s" % self.name)
    
class SpecialEmployee(Employee):
    
    def __init__(self, name, rate, bonus):
        super().__init__(name, rate) # calls the base classes
        self.bonus = bonus

    def hours(self, numHours):
        self.owed += numHours*self.rate + self.bonus
        return ("%.2f hours worked " % numHours )
    
# using issubclass() to check whether a class is a subclass of another class
# using isinstance() to check if an object belongs to a class or not
print(issubclass(SpecialEmployee, Employee)) # True
print(issubclass(Employee, SpecialEmployee)) #False

sp = SpecialEmployee("pactk",20,100)
emp = Employee("packt",20)
print(isinstance(sp,Employee)) # True
print(isinstance(emp,SpecialEmployee)) # False