class Demo:
    a=4
o=Demo()
print(o.a)# prints the class attribute bcz instance atribute is not present
o.a=0 # Here we can change anything by instance attribute but we can not change the class attribute
print(o.a)
print(Demo.a) #prints class attribute
