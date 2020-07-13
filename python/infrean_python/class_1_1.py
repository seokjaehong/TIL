
#Chapter-02-01

## 3. 딕셔너리 구조
# 코드반복지속, , 중첩문제(키)  , 키 조회 예외처리 등


car_dict = [
    {
        'car_company': 'Ferrari',
        'car_detail': {
            'color': 'White',
            'horsepower': 400,
            'price': 8000
        }
    },
    {
        'car_company': 'BMW',
        'car_detail': {
            'color': 'Black',
            'horsepower': 270,
            'price': 5000
        }
    },
    {
        'car_company': 'Audi',
        'car_detail': {
            'color': 'Silver',
            'horsepower': 300,
            'price': 6000
        }

    }
]


# del car_dict[1]
# print(car_dict)

## 4.클래스구조
# 구조 설계후 재사용성 증가, 코드반복 최소화 , 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        # 사용자가 정보확인
        return ' str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        # 엔지니어가 객체의 엄격한 타입, 정보 를 확인 .. 무슨말이지
        # __str__이 없으면 __repr__ 이 출력됨
        return ' repr: {} - {}'.format(self._company, self._details)


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
print(car1)
print(car2)
print(car3)

# 중간중간에 들어 있는 속성
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))
print()
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)  ## repr

for x in car_list:
    print(x)  ## str
