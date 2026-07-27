
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

person = Person("Caleb ,Han", "2000-10-10")
print(person.is_adult())
print(person.screen_name())