#Date: November 16, 2018

userName = input("Welcome to the Calculator. \nWhat is your name: ")
print("Welcome " + userName.strip().title() + "!")
print("\nWe only accept numbers between 0 and 100")

tooLow = ("Your number is too low!")
tooHigh = ("Your number is too high!")

firstNumber= float(input("Please enter your first number: "))
if firstNumber <0:
    print(tooLow)
elif firstNumber >100:
    print(tooHigh)
else:
    print("good selection!")

secondNumber= float(input("Please enter your second number: "))
if secondNumber <0:
    print(tooLow)
elif secondNumber >100:
    print(tooHigh)
else:
    print("good selection")

print('{} + {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber+secondNumber)

print('{} - {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber-secondNumber)

print('{} * {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber*secondNumber)

print('{} / {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber/secondNumber)

print("\nThank you!")
