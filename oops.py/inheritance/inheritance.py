# It is called base class or parent class
class Employee:
    company="ITC"
    salary=1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


#class Programmer:
    #company="ITC Infotech"
    #def show(self):
    #    print(f"The name is {self.name} and the salary is {self.salary}")

    #def showLanguage(self):
        #print(f"The name is {self.name} and he is good with {self.language} language ")

#It is called inheritance class
class Programmer(Employee):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")

a=Employee()
b=Programmer()

print(a.company,b.company,a.salary)
print(type(a.salary))