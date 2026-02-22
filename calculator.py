# simple_calculator.py
# A simple calculator that performs basic arithmetic operations.

print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: +  -  *  /")
choice = input("Enter operation: ")

if choice == "+":
    print("Result =", num1 + num2)

elif choice == "-":
    print("Result =", num1 - num2)

elif choice == "*":
    print("Result =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid operation.")