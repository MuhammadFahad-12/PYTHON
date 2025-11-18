a = int(input("Enter a: "))
b = int(input("Enter b: "))
operator = int(input("Enter operator (1:Add, 2:Subtract, 3:Multiply): "))

if operator == 1:
    print(a + b, end="")
elif operator == 2:
    print(a - b, end="")
elif operator == 3:
    print(a * b, end="")
else:
    print("Invalid Input", end="")