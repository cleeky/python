import datetime as date


class Person:
    def __init__(self, first_name, second_name, date_of_birth):

        self.first_name = first_name
        self.second_name = second_name
        day, month, year = date_of_birth.split("/")
        today = date.date.today()
        self.date_of_birth = date.date(int(year), int(month), int(day))
        self.age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.second_name)


per1 = Person("Colin", "Leek", "22/01/1969")

print('Name: {}\nAge: {}'.format(per1.fullname, per1.age))
