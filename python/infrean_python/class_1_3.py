# Chapter-02-03

class Car():
    """
    Car Class
    Author : Hong
    Date : 2020.7.13
    Description : Class ,Static, Instance Method
    """
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.2

    def __init__(self, company, details):
        # 보통 인스턴스변수는 앞에 언더바를 붙여준다.
        self._company = company
        # self.car_count=10
        self._details = details

    def __str__(self):
        return ' str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return ' repr: {} - {}'.format(self._company, self._details)

    # Instance Method
    # self: 객체의 고유한 속성 값을 사용

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('color')))

    # Instance Method
    def get_price(self):
        # 내부에서는 get함수를 쓰는 것이 좋다
        return 'Before Car Price -> Company : {}, price:{}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> Company : {}, price:{}'.format(self._company,
                                                                  self._details.get('price') * Car.price_per_raise)

    # class Method(cls : class 를 받는다)
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # static method ( google research : static method vs class method )
    # 아무 인자도 받지않는다. (공통적으로 유연한 메소드를 만들때 쓰는것이 좋다)
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This Car is {}'.format(inst._company)

        return 'Sorry. This Car is not BMW'


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

car1.detail_info()
car2.detail_info()

# 가격정보(직접접근)
# 좋지 않은 방법 (이것을 하지 못하게 private로 막아놓는다)
# print(car1._details.get("price"))
# print(car1._details['price'])

# 가격정보(인상전)
print(car1.get_price())
print(car1.get_price_culc())

# 가격인상(클래스메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상후)
print(car1.get_price())
print(car1.get_price_culc())

# 가격정보(클래스메소드 사용 인상 후)
Car.raise_price(1.6)
print(car1.get_price())
print(car1.get_price_culc())

# 스태틱메서드
# 인스턴스호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 호출 (스태틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))