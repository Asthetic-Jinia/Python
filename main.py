'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youDic={"s":1,"w":-1,"g":0}
reverseDic={1:"Snake", -1:"Water", 0:"Gun"}
you=youDic[youstr]

print(f"You chose {reverseDic[you]}\n Computer chose {reverseDic[computer]}")

if(computer==you):
    print("It's draw")
else:
    if(computer==-1 and you==1):
      print("You win!")

    elif(computer==-1 and you==0):
          print("You lose!")

    elif(computer==1 and you==-1):
        print("You lose!")

    elif(computer==1 and you==0):
       print("You win!")

    elif(computer==0 and you==-1):
        print("You win!")

    elif(computer==0 and you==1):
        print("You lose!")

    else:
        print("something went wrong")

''' or we can write this logic
if((computer-you)==-1 or (computer- you)==2):
   print("You lose!")
else:
   print("You win!")
'''