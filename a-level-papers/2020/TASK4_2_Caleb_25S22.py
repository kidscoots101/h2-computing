
class Person:
    def __init__(self, name, birth):
        self.full_name = name
        self.date_of_birth = birth

    def is_adult(self):
        return 2026 - int(self.date_of_birth[0:4]) >= 18
    def screen_name(self):
        pass


person = Person("Caleb", "2000-10-10")
print(person.is_adult())