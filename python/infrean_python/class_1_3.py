#Chapter-02-03

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
