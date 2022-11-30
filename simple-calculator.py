choice = input("addition, subtraction, multiplication, divide: ")

a = int(input("first number: "))
b = int(input("second number: "))

if (choice == "addition"):
    print(a + b)
elif (choice == 'subtraction'):
    print(a - b)
elif (choice == 'multiplication'):
    print(a * b)
elif (choice == 'divide'):
    print(a / b)
else:
    print("wrong choice")
