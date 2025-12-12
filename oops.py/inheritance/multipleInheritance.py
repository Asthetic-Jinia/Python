# It is called base class or parent class
class Employee:
    company="ITC"
    name="Default name"
    salary=1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder:
    language="Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


#It is called inheritance class
# Here Employee and coder both is the parent of Programmer
class Programmer(Employee,coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language ")

a=Employee()
b=Programmer()


b.show()
b.printLanguages()
b.showLanguage()
