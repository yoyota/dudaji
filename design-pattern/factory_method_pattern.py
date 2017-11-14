"""
from
https://en.wikipedia.org/wiki/Factory_method_pattern#Python
"""
from abc import ABCMeta, abstractmethod
from enum import Enum


class Person(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError("You should implement this!")


class Villager(Person):
    def get_name(self):
        return "Village Person"


class CityPerson(Person):
    def get_name(self):
        return "City Person"


class PersonType(Enum):
    RURAL = 1
    URBAN = 2


class Factory:
    def get_person(self, person_type):
        if person_type == PersonType.RURAL:
            return Villager()
        elif person_type == PersonType.URBAN:
            return CityPerson()
        else:
            raise NotImplementedError("Unknown person type.")


factory = Factory()
person = factory.get_person(PersonType.URBAN)
print(person.get_name())