"""
In python object class is parent class of all classes, like Build-in str,int and
custom types
"""


class Dog:
    """
    properties are actually called attributes,
    class attribute are the same for each instance, can be a default for the class
    but they can be changed on each class differently
    """
    species = "mammal"

    def __init__(self, name, age):
        # self is used to the current object being initiated
        """
        self.age are instance attributes and they are independent for each class object
        """
        self.name = name
        self.age = age

    def description(self):
        """
        this class method are called instance method in python
        :return:
        """
        return f"{self.name} is {self.age} years old"


class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    def eat(self, food):
        print(f"{self.name} eats {food}")


class Baby(Person):
    # this is called overwriting
    description = "general person"

    def speak(self):
        print("ba ba ba ba ba")

    def nap(self):
        print(f"{self.name} takes a nap")


if __name__ == '__main__':
    a = Dog("lucky", 10)
    # type will give the type of the object
    print(type(a))
    # see if an object is a specific type
    print(isinstance(a, Dog))
    print(isinstance(a, object))


