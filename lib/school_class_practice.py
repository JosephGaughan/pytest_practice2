class School:
    def __init__(self, name, location, pupils):
        if pupils < 0:
            raise Exception("Number of pupils cannot be nagative.")
        self.name = name
        self.location = location
        self.pupils = pupils
        self.register = []

    def school_age(self, year_founded):
        current_year = 2025
        self.age = current_year - year_founded
        return self.age
    
    def school_students(self):
        return self.register
    
    def add_student(self, student):
        self.register.append(student)

school_example = School("St Example", "Preston", 100)

print(f"{school_example.name} is based in {school_example.location} and has {school_example.pupils} pupils.")

print(f"Also, the school is {school_example.school_age(2000)} years old.")

# ----------------- Creating a New Class ----------------------

class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        school.add_student(self, name)    