class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

    def __del__(self):
        print("Destructor called")


# Create an object
student1 = Student("Rahul", 101)

# Call the method
student1.display()

# Delete the object
del student1