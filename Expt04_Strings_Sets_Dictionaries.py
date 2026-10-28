# String
text = "Python Programming"

print("String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reversed:", text[::-1])

# Set
numbers = {10, 20, 30, 20, 40}
numbers.add(50)

print("\nSet:", numbers)
print("Set union:", numbers.union({60, 70}))
print("Set intersection:", numbers.intersection({20, 30, 80}))

# Dictionary
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE"
}

print("\nStudent details:", student)
print("Name:", student["name"])

student["year"] = "Third Year"
print("Updated dictionary:", student)