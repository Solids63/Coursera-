import json


class ExportJSON:
    def to_json(self):
        return json.dumps({
            'name':  self.name,
            'breed': self.breed
        })




class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return '{0}: waw'.format(self.name)

    def get_breed(self):
        return self.__breed


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        #  Вызов метода по МРО
        super().__init__(name, breed)
    #  super(ExDog, self).__init__(name)


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        #  явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = 'Шерстяная собака породы {0}'.format(_Dog__breed)


dog = ExDog('Тузик', "Питбуль")
print(dog.get_breed())
print(dog.__dict__)
