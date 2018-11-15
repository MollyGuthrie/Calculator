#Date: November 15, 2018

print("Calculator Program")

userName = input("What is your name: ")
print("Welcome " + userName.strip().title() + "!")

firstNumber= float(input("Please enter your first number: "))
secondNumber= float(input("Please enter your second number: "))

print('{} + {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber+secondNumber)

print('{} - {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber-secondNumber)

print('{} * {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber*secondNumber)

print('{} / {} = '.format(firstNumber, secondNumber), end="")
print(firstNumber/secondNumber)
