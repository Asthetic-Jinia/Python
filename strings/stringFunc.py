name="harry is a good boy"
print(len(name))
print(name.endswith("rry"))
print(name.count("r"))
print(name.capitalize())
print(name.find("r"))
print(name.replace("good","bad"))

# f string

name=input("Enter your name: ")
print("Good Afternoon," ,name)
# or we can use f string

print(f"Good Afternoon,{name}")

# chaining of .replace
letter='''Dear <|Name|>,
You are selected !
<|Date|>'''
print(letter.replace("<|Name|>","Harry").replace("<|Date|>","24 September 2025"))

# Detect the index of double space
name="Harry is  a good boy"
print(name.find("  "))