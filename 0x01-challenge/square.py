#!/usr/bin/python3

class Square():
    
    side = 0

    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def perimeter_of_my_square(self):
        return self.side * 4

    def __str__(self):
        return "{}x{}".format(self.side, self.side)

if __name__ == "__main__":

    s = Square(side=12)  # Make sure to provide only one side length
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
