class Square:
        def __init__(self, lenght):
            self.lenght = lenght
        def area(s, area_1 = 0):
            print(area_1)
class Shape(Square):
    pass 


cl_1 = Shape(12)
cl_1.area()
cl_1.area(12)



