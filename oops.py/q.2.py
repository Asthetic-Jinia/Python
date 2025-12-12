# Write a class"Calculator" to find square,cube and square root of a number
class calculator:
    def __init__(self,n):
       self.n=n
    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n* self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n **1/2}")
    @staticmethod
    def hello():
        print("Hello world!") # staticmethod is used if I dont want to add any instance attribute

a=calculator(4)

a.square()
a.cube()
a.squareroot()
a.hello()
