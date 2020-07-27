# Chapter 04-03
# 시퀀스형
# 1-1.Container : 서로 다른 자료형을 담을 수 있다.
# list , tuple , collections.deque
# ex) a = [3, 3.0, 'a']
# 1-2.Flat : 하나의 자료형만 담을수 있다.( 그래서 더 빠름)
# str, bytes, bytearray, array.array, memoryview

# 2-1.가변(List, bytearray, array.array, memoryview, collections.deque)
# 2-2.불변(tuple,str, bytes)

# 해시테이블 : Key에 value를 저장하는 구조 , 파이썬 자체가 해시테이블로 만들어져잇닥
# 파이썬 dict 해시(고유한값같은거) 테이블 예
# 키값의 연산 결과에 따라 직접접근이 가능한 구조, 파이썬은 dict를 그냥 쓰면됨
# key값을 해싱함수 -> 해쉬 주소 -> key에 대한 value 참조
# 키가중복되면 내부적으로 어떻게 처리하나 (이런질문)

# Dict 구조
# print(__builtins__.__dict__)

# Hash값 확인 -> 이말은 고유하다
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

# print(hash(t1))  # <-- hash안에 들어가는건 불변형 (immutable이어야함 )
# print(hash(t2))

print()
print()

# Dict Setdefault예제 (tuple -> dict 할때 강추함)
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use SetDefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# user SetDefault ; 와 이거 짱이네..
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)

# 주의, 이렇게 하면 안댐
new_dict3 = {k: v for k, v in source}
print(new_dict3)

print()
print()

