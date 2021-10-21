import random
number = random.randint(0,5)
name = input("Enter your name: ")
print("hello {}!".format(name))
def guess_number():
    counter=0
    while counter <3:
        counter +=1
        guess_number = int(input("Guess the number: "))
        if(number==guess_number):
         print("gotcha you are right..!")
         break
        elif(number>guess_number):
         print("Oops Too low")
        else:
         print("Oops Too high")
    if(number!=guess_number):
        print("your chances are over better luck next time..!")     
guess_number()