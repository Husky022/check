class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        RadiusVector2D.set_x(self, x)
        RadiusVector2D.set_y(self, y)

    def set_x(self, x):
        if x in range(RadiusVector2D.MIN_COORD, RadiusVector2D.MAX_COORD):
            self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        if y in range(RadiusVector2D.MIN_COORD, RadiusVector2D.MAX_COORD):
            self.__y = y

    def get_y(self):
        return self.__y

    @staticmethod
    def norm2(vector):
        return vector.get_x() ** 2 + vector.get_y() ** 2

    x = property(get_x, set_x)
    y = property(get_y, set_y)



v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)
r5 = RadiusVector2D(-89, 2000)

print(v1.x, v1.y)
print(v2.x, v2.y)
print(v3.x, v3.y)
print(r5.x, r5.y)
