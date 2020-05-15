from pprint import pprint


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        return 'Rectangle'


class Square(Rectangle):
    def __init__(self, length):
        """
        super allows to access the parent methods
        """
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


class Cube(Square):
    def surface_area(self):
        """
         when we call self it will look for the method there and if it does not find it
        he will start searching in the parent for the function.
        if it does not find the method he will call an AttributeError
        """
        face_area = self.area()
        return face_area * 6

    def volume(self):
        """
        here when using super it look directly in the parent without looking in the child first
        :return:
        """
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i() + ' child of ' + super(Cube, self).what_am_i()


if __name__ == '__main__':
    cube = Cube(3)
    square = Square(3)
    # with dir on a class you can see a lot of data about it
    pprint(dir(square))
    """
    super inside a class it just a shortcut for super(my_class, self)
    the regular syntax is super(class, object)
    here will go to the parent and will use his method
    """
    print(super(Cube, cube).what_am_i())
    """
    here it will go the the parent of square 
    that how super allows you to access all the method in the class hierarchy 
    """
    print(super(Square, cube).what_am_i())

