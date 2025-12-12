name="jinia" # length of string 5
nameshort=name[0:3] #start from index 0 all the way 3 (excluding 3)
print(nameshort)
character1=name[1]
print(character1)

# Negetive Slicing

print(name[-4:-1]) # we have to count as -1,-2,-3....from the end of the string
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

# Slicing with skip value

b="abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4]) # (b,f)