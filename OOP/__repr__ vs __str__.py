import datetime


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        """
        it iss  a dander method it's a core python thing
        the underscore it's king of a conviction to namespace them so class will not
        create their own dander method and create conflict with python core in the future
        any time str() is used on a class this method is called , event if a function like print does it
        intently
        """
        # now when you print it you will see this, cus he covert the method to str
        return f"a {self.color} car"

    def __repr__(self):
        """


        """
        # you can get the name of the class with the first line
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'


if __name__ == '__main__':
    my_car = Car("red", 378413)
    # calls __str__ and then prints it format also does that
    print(my_car)
    # juts like that will call the __repr__
    my_car
    # you can also force the repr function with
    print(repr(my_car))
    today = datetime.date.today()
    # will call the __str__ and will return nice representation of the date
    print(today)
    # will return something like datetime.date(2020, 5, 14)
    print(repr(today))
    # __str__ ==> easy to read , for human consumption, user
    # __repr__ ==> unambiguous more easy for developer to debug (can be an object you can just return and run again)
    """
    # if you don't define str implantation it is recommended to define ,
    a repr on every class so you will get a readable result in all cases 
    """
    # when you call str in a container it will use the objects repr
    print([today, today, today])

