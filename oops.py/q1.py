#create a class "programmer" for storing the info of microsoft employee
class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Jinia",1200000,721151)
print(p.name,p.salary,p.pin,p.company)

p=Programmer("Kaustav",1800000,721151)
print(p.name,p.salary,p.pin,p.company)