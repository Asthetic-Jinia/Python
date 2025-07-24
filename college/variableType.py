
var = input("Enter a value: ")


print("Type of the variable:", type(var))

try:
    var = float(var)
    print("Type of the variable after conversion:", type(var))
except ValueError:
    print("The input cannot be converted to a number.")