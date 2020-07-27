# Chapter03-02
# Special Method ( magic method )
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 파이썬의 핵심 (
# 1.시퀀스(sequence) ,2.반복(iterator),
# 3.함수(Functions), 4.클래스(Class) )

# 기본형
# print(int(10))
# print(int)
# print(float)

# 모든 속성 및 메소드 출력
# print(dir(int))
# print(dir(float))

n = 10
# print(type(n))

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)

print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))


#############################################

# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {}, {} '.format(self._name, self._price)

    # def __add__(self, other):
    #     print('called >> __add__')
    #     return int((self._price + other._price) * 0.8)

    def __sub__(self, other):
        print('called >> __sub__')
        return self._price - other._price

    def __le__(self, other):
        print('called >> __le__')
        if self._price <= other._price:
            return True
        return False

    def __ge__(self, other):
        print('called >> __ge__')
        if self._price >= other._price:
            return True
        return False


s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)
s3 = Fruit("Canana", 2000)

# builtin안해놓는다면,, 일반적인 계산이고, Add method를 사용하는 게좋다
print(s1._price + s2._price+s3._price)

# magic method를 구현해놓으니까 짱 좋음..
# print(s1 + s2)
# 근데 함부로 하면 에러가 나눈군
# print(s1 + s2 + s3)

# print(s1 - s2)
# print(s1 >= s2)
# print(s1 <= s2)

# python base model link check check check