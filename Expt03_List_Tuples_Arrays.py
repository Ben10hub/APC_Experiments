from array import array

# List
numbers = [10, 20, 30, 40]
numbers.append(50)

print("List:", numbers)
print("First element:", numbers[0])

# Tuple
values = (10, 20, 30, 40)

print("Tuple:", values)
print("Tuple length:", len(values))

# Array
arr = array('i', [1, 2, 3, 4, 5])
arr.append(6)

print("Array:", arr.tolist())
print("First array element:", arr[0])

print("List length:", len(numbers))
print("Tuple maximum:", max(values))
print("Array sum:", sum(arr))