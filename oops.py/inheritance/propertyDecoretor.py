class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    #it is called abstruction means we have hidden the implementation details from the user
   # encapsulation  means we have packed many working components in a perticular unit which is class here
e=Employee()
e.a=45 #If we don't use @classmethod then 45 would be printed
e.name="Harry Khan"
print(e.name)
e.show()