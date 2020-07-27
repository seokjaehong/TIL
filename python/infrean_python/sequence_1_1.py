# Chapter 04-01
# 시퀀스형
# 1-1.Container : 서로 다른 자료형을 담을 수 있다.
# list , tuple , collections.deque
# ex) a = [3, 3.0, 'a']
# 1-2.Flat : 하나의 자료형만 담을수 있다.( 그래서 더 빠름)
# str, bytes, bytearray, array.array, memoryview

# 2-1.가변(List, bytearray, array.array, memoryview, collections.deque)
# 2-2.불변(tuple,str, bytes)

# 3. 리스트 및 튜플 고급

# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!)'
code_list1 = []
for s in chars:
    # 유니코드리스트
    code_list1.append(ord(s))
print(code_list1)

# Comprehending lists
code_list2 = [ord(x) for x in chars]
print(code_list2)

# Comprehending lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

# print(map(ord,chars))
# print(list(map(ord,chars)))
print(code_list4)

print([chr(x) for x in code_list1])
print([chr(x) for x in code_list2])
print([chr(x) for x in code_list3])
print([chr(x) for x in code_list4])

print()
print()

# Generator 생성
# iterator를 생성해주는 함수 , 다음에 내가 반환할 위치정보만 갖고있어서, 메모리 사용량이 작아

# print(dir(chars)) -- > __iter__ 체크
import array

# Generator : 한번에 한개의 항목을 생성(메모리 유지를 하지않는다 )
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(next(tuple_g))
print(array_g)
print(type(array_g))
print(array_g.tolist())

print()
print()

# 제네레이터 예제

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s, end=' ')

print()
print()
# 리스트 주의
# 깊은복사 / 얕은복사 (deep copy, shallow copy)

marks1 = [['~'] * 3 for _ in range(4)]
print(marks1)

marks2 = [['~'] * 3] * 4
print(marks2)

# print(marks1, marks2)

# 수정
marks1[0][1] = 'x'
print(marks1)  # --> 내가 지정한 것만 바뀜
marks2[0][1] = 'x'
print(marks2)  # --> 헐 다바뀜 ..
# 결과값이 아예다름..

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])  # --> 아 id 가 모두 동일하구나 (*) 이걸로 복사했으니까
# 실제 서비스할 때 이렇게 해주면 큰일나겠다
