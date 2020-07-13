#Chapter-02-02
class Car():
    """
    Car Class
    Author : Hong
    Date : 2020.7.13
    Description : check
    """
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        # 보통 인스턴스변수는 앞에 언더바를 붙여준다.
        self._company = company
        self._details = details
        # self.car_count=10
        Car.car_count += 1

    def __str__(self):
        return ' str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return ' repr: {} - {}'.format(self._company, self._details)

    def __del__(self):
        print('del?')
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('color')))


# self의미
car1 = Car('Ferrari', {
    'color': 'White',
    'horsepower': 400,
    'price': 8000
})
car2 = Car('BMW', {
    'color': 'Black',
    'horsepower': 270,
    'price': 5000
})
car3 = Car('Audi', {
    'color': 'Silver',
    'horsepower': 300,
    'price': 6000
})

# ID값 확인
# print(id(car1))
# print(id(car2))
# print(id(car3))

car1.detail_info()
car2.detail_info()
car3.detail_info()

# print(car1._company == car2._company)
# print(car1 is car2)

# print(car1.__dict__)
# print(car2.__dict__)

# print(Car.__doc__)
# print()

# print(car1.__class__,car2.__class__)


# 에러 발생
# Car.detail_info()

# 에러 No 발생
# Car.detail_info(car1)
# car1.detail_info()

print()
## 클래스변수 실습부분(클래스변수 공유 확인 )
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근방법
print(car1.car_count)
print(Car.car_count)

# 삭제확인
del car2
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색함
# 즉, 동일한 이름으로 변수생성이 가능함(인스턴스 검색 후 -> 상위(클래스변수,부모클래스 변수를 )
# init에 car_count =10 선언해도 상위에 car_count가 있기 때문에 상위클래스변수다음에 찾음, 그래도 없으면 에러
