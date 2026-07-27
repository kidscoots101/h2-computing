
# Task 4.2

class Person:
    def __init__(self, name, birth):
        self.full_name = name
        self.date_of_birth = birth

    def is_adult(self):
        return 2026 - int(self.date_of_birth[0:4]) >= 18
    def screen_name(self):
        full = ""
        for char in self.full_name:
            if char.isalpha() == True:
                full += char
        date = self.date_of_birth.split("-")
        return full + date[1] + date[2]        

person = Person("Caleb Han", "2000-10-10")
print(person.is_adult())
print(person.screen_name())
print("")

# for staff
class Staff(Person):
    def __init__(self, name, birth):
        super().__init__(name, birth)
    def is_adult(self):
        return True
    def screen_name(self):
        return super().screen_name() + "Staff"

staff = Staff("Aloysius Lee", "2000-05-19")
print(staff.screen_name())
print(staff.is_adult())
print("")

# for students

class Student(Person):
    def __init__(self, name, birth):
        super().__init__(name, birth)
    def is_adult(self):
        return False

student = Student("Nolan Tan", "2019-09-22")
print(student.screen_name())
print(student.is_adult())
print("")