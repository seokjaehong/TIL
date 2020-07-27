# Chapter03-02
# Special Method ( magic method )

# 파이썬의 핵심 (
# 1.시퀀스(sequence) ,2.반복(iterator),3.함수(Functions), 4.클래스(Class) )
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 클래스 예제2
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    def __init__(self, *args):
        """
        Create a vector,
        Example : v = Vector(5,10)

        :param args:
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        return the vector information
        :return:
        """
        return 'Vector ({}, {})'.format(self._x, self._y)

    def __add__(self, other):
        """
        Return the vector addition of self and other
        :param other:
        :return:
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        print('warning!! 0,0')
        return bool(max(self._x, self._y))

    def __le__(self, other):
        return Vector(self._x - other._x, self._y - other._y)


v1 = Vector(1, 2)
v2 = Vector(5, 5)
v3 = Vector()
print(v1, v2, v3)

print(v1 + v2)
print(v1 * 5)
print(v1 - v2)
print(v2 * 100)
print(bool(v1), bool(v3))

# print(Vector.__init__.__doc__)
# print(Vector.__add__.__doc__)
# print(Vector.__repr__.__doc__)
