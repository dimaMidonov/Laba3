class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            raise ValueError("Рост не может быть отрицательной")
        self._height = height



person = Person("Anna", 25, 170)
person.set_name("Tom")


print(person.get_name())  # выведет "Tom"





#ИСПОЛЬЗОВАНИЕ @property
class Person:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Рост не может быть отрицательной")
        self._height = height


person = Person("Anna", 25, 170)
person.name = "Tom"


print(person.name)  # выведет "Tom"

