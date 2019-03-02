from test1 import Person


class Employee(Person):
    def __init__(self, name, surname, age, position, salary):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.position = position
        self.salary = salary

    def money(self, monthes):
        return f'In {monthes} monthes time money budet{int(self.salary) * monthes}'


if __name__ == "__main__":
   e1 = Employee(name='Vasiliy',surname='vasin',age='44',position='cleaner',salary='1000')