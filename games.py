from time import sleep
from os import system

name = input("What is your name?")
print(" Hello " + name)

sleep(2)

system("cls")

print("You are curently late to a party your invited to and you got lost.")


print("What do you do?")
print()
print("A. You drive left")
print("B. You drive right")

choice = input()
if choice == "A" :
    print ("You have chosen left")
    sleep(2)
    system("cls")
    print ("Oh no! You landed in traffic")
    sleep(2)
    print ("Do you wish to continue?")
    print ("Yes")
    print("No")

decision = input()
if decision == "Yes" :
    print ("You have chosen to continue and you actually made it on time")
    print ("Hooray! You have completed the game!")

elif decision == "No" :
    print ("You have chosen to go home and your car exploded")
    print ("and now your Dead...")
elif  choice == "B" :
    print ("You have chosen right")
    print ("You have made more earlier than you expected")
    print ("Hooray! You have completed the game!")
else :
    print("Try again?")
