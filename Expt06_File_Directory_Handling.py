import os

# Create and write to a file
with open("sample.txt", "w") as file:
    file.write("Welcome to Python programming.\n")
    file.write("This is a file handling example.")

print("File created successfully.")

# Read the file
with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile content:")
print(content)

# Append content
with open("sample.txt", "a") as file:
    file.write("\nThis line is appended.")

# Display current directory
print("\nCurrent directory:", os.getcwd())

# Display files and folders
print("Directory contents:", os.listdir("."))