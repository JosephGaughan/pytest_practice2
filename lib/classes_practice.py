class Person:

    species = "Human Being"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")


class Dog:

    sound = "unspecified dog sound"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
    
    # Example of a standard method within a class (instance method).
    # def bark(self):
    #     print("Woof!")

    @classmethod
    def make_sound(cls):
        # This class method accesses the class variable `sound`
        print(cls.sound)

    # Example of a static method within a class (this does not require an instance of the class (also known as an object)).
    @staticmethod
    def bark():
        print("Woof!")

person_joe = Person("Joe", 23, "Preston")

# Printing attributes (variables) of the 'Person' class to understand attributes "instance variables".
print(person_joe.name, person_joe.age)
print(person_joe.species)

# Changing Class Variable 'species' to understand class variables.
person_joe.species = "mammal"
print(person_joe.species)
dog_tyson = Dog("Tyson", "Bully")

print(dog_tyson.breed)

# Running a method (function) from the 'person' class to understand instance methods.
person_joe.celebrate_birthday()

# For testing instance vs static variables. This can be used for both.
dog_tyson.bark()

# This prints the predeterminded (class method) dog sound.
dog_tyson.make_sound()
# For testing method variables. This now prints "RaRaRarrrrr!" instead of the predetermined "unspecified dog sound".
Dog.sound = "RaRaRarrrrr!"
dog_tyson.make_sound()

print("*******************************")

# This avoids using __init__ and instead requires input before the attributes are held
class Cat:
    def cat_details(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

cat_sparkles = Cat()

cat_sparkles.cat_details("Sparkles", "short hair", 10)

print(cat_sparkles.name)

print("*******************************")

# Here is the equivalent that makes use of __init__ by modifying it to store attributes

class Rabbit:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

rabbit_daisy = Rabbit("Daisy", "Minnature Rabbit", 2)

print(rabbit_daisy.name)