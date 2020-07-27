# Chapter03-03
# Special Method ( magic method )

# 파이썬의 핵심 (
# 1.시퀀스(sequence) ,2.반복(iterator),3.함수(Functions), 4.클래스(Class) )
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 객체 -> 파이썬의 데이터를 추상화
# 모든객체 -> id , type -> value

# (1) 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# (2) named tuple 사용
from collections import namedtuple

# namedtuple 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(pt3[0], pt3.x)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng2)

# (3) 네임트 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default =False

# 예약어는 사용할  없다. rename으로 사용가능


# 출력
print("###출력###")
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dic = {'x': 75, 'y': 55}

# 객체 생성

p1 = Point1(x=10, y=35)
print(p1)
p2 = Point2(20, 40)
print(p2)
p3 = Point3(45, y=20)
print(p3)
p4 = Point4(10, 20, 30, 40)
print(p4)  # key를 난수로 생성 , 그래서 자주쓰이지는 않음

p5 = Point3(**temp_dic)
print(p5)

x, y = p2
print(x, y)

# namedtuple의 method
# 1._make() : 리스트를 기반으로 새로운 객체를 생성
temp = [52, 38]
p7 = Point1._make(temp)
print(p7)

# 2. _fields() : 필드네임을 확인할 수 있게함
print(p1._fields, p4._fields)

# 3. _asdict(): OrderedDict를 반환
print(p1._asdict())
##############################
## 실 사용 실습
# 한반에 20명, 4개의 반(A,B,C,D) 예제)  B14 D18

Classes = namedtuple('Classes', ['rank', 'number'])
# 그룹 리스트 선언
numbers = [str(x) for x in range(1, 21)]
ranks = 'A B C D'.split()
# print(numbers,ranks)

students = [Classes(rank, number) for rank in ranks for number in numbers]
# print(len(students))

# 추천 방법(한줄로구성)
students2 = [Classes(rank, number) for rank in 'A B C D'.split() for number in [str(x) for x in range(1, 21)]]
# print(students2)


# 출력
for s in students:
    print(s)
