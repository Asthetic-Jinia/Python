class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=Employee()
e.a=45 #If we don't use @classmethod then 45 would be printed
e.show()