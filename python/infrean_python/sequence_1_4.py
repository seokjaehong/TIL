# Chapter 04-04
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 하지 않음, Set -> 중복허용x
# Dict 및 Set 심화

# immutable dict (읽기전용 Dict라고 봐도됨)
from types import MappingProxyType

# 수정가능
# d = {'key1': 'value1'}
# d['key1'] = 0
# print(d)

d = {'key': 'value1'}
# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정불가, d

# d_frozen['key2'] = 0
# print(d_frozen)


print()
print()

# SET (순서 뒤죽박죽)

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})  # 정말 중요한 것들
print(s1)

s1.add('Melon')
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# set 선언최적화
# 바이트 코드 -> 파이썬 인터프리터가 실행
# from dis import dis
#
# print('--------')
# print(dis('{10}'))
# print('--------')
# print(dis('set([10])'))


# 지능형 집합 (comprehending set)

print('----------------')
from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
