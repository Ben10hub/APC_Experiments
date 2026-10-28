
name = input("Enter your name: ")
age = int(input("Enter your age: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division is not possible")

print("Python supports variables, data types, operators and conditions.")