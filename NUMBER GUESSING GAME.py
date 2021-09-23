import random
mynum=random.randint(0,9)

print("I have a number in mind can you guess it")
while  True:
    usernum=int(input("enter your guess : "))
    if(mynum==usernum):
        print("nice guess")
        break
    elif(mynum>usernum):
        print("my number is greater.tryagain")
    else:
        print("my  number is smaller.tryagain")
