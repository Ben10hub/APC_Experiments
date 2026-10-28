# User-defined function
def add(a, b):
    return a + b

def square(n):
    return n * n

print("Addition:", add(10, 20))
print("Square:", square(5))

# Lambda function
multiply = lambda a, b: a * b

print("Multiplication:", multiply(4, 5))

# Lambda with filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)