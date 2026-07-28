
# Task 4.2

import sqlite3

class Person:
    def __init__(self, name, birth):
        self.full_name = name
        self.date_of_birth = birth

    def is_adult(self):
        return 2026 - int(self.date_of_birth[0:4]) >= 18 # checks whether it's above 18 or not
    def screen_name(self):
        full = ""
        for char in self.full_name:
            if char.isalpha() == True: # logic to remove spaces, punctuations
                full += char
        date = self.date_of_birth.split("-")
        return full + date[1] + date[2]        

'''
person = Person("Caleb Han", "2000-10-10")
print(person.is_adult())
print(person.screen_name())
print("")
'''

# for staff
class Staff(Person): # inherits Person class
    def __init__(self, name, birth):
        super().__init__(name, birth)
    def is_adult(self):
        return True
    def screen_name(self):
        return super().screen_name() + "Staff"
    
'''
staff = Staff("Aloysius Lee", "2000-05-19")
print(staff.screen_name())
print(staff.is_adult())
print("")
'''

# for students

class Student(Person):
    def __init__(self, name, birth):
        super().__init__(name, birth)
    def is_adult(self): # sets to False by default
        return False
'''
student = Student("Nolan Tan", "2019-09-22")
print(student.screen_name())
print(student.is_adult())
print("")
'''

with open('people.txt', 'r') as file:
    file = file.read().strip().split("\n") # 'John Tan,2000-06-01,Person'
    connection = sqlite3.connect("school.db")
    for obj in file:
        obj = obj.split(",")
        name = obj[0]
        DOB = obj[1]
        class_t = obj[2]
        if class_t == "Person": # condition to check through what class type
            person = Person(name, DOB)
            screen_name = person.screen_name()
            is_adult = person.is_adult()
            connection.execute(
                f'''
                INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES(?, ?, ?, ?)
                ''', # SQL logic to insert into database school.db
                (name, DOB, screen_name, is_adult) # 
            )
        elif class_t == "Student":
            student = Student(name, DOB)
            screen_name = student.screen_name()
            is_adult = student.is_adult()
            connection.execute(
                f'''
                INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES(?, ?, ?, ?)
                ''',
                (name, DOB, screen_name, is_adult)
            )

        elif class_t == "Staff":
            staff = Staff(name, DOB)
            screen_name = staff.screen_name()
            is_adult = staff.is_adult()
            connection.execute(
                f'''
                INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES(?, ?, ?, ?)
                ''',
                (name, DOB, screen_name, is_adult)
            )
    connection.commit()
    connection.close()
