class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)

class Rectangle:

    def __init__(self, *agrs):
        self.lst = agrs
        if len(self.lst) == 2:
            self.__sp = self.lst[0].get_coords()
            self.__ep = self.lst[1].get_coords()
        else:
            self.__sp = (self.lst[0], self.lst[1])
            self.__ep = (self.lst[2], self.lst[3])

    def set_coords(self, sp, ep):
        self.__sp = sp.get_coords()
        self.__ep = ep.get_coords()

    def get_coords(self):
        a = Point(self.__x1, self.__y1)
        b = Point(self.__x2, self.__y2)
        return (a, b)

    def draw(self):
        print(f"Прямоугольник с координатами: ({self.__sp[0]}, {self.__sp[1]}, {self.__ep[0]}, {self.__ep[1]})")

rect = Rectangle(0, 0, 20, 34)