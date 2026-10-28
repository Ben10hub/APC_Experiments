# Inheritance
class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Objects
animal = Animal()
dog = Dog()
cat = Cat()

print("Inheritance and Polymorphism:")

animal.sound()
dog.sound()
cat.sound()