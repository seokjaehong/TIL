# Chapter 04-02
# 시퀀스형
# 1-1.Container : 서로 다른 자료형을 담을 수 있다.
# list , tuple , collections.deque
# ex) a = [3, 3.0, 'a']
# 1-2.Flat : 하나의 자료형만 담을수 있다.( 그래서 더 빠름)
# str, bytes, bytearray, array.array, memoryview

# 2-1.가변(List, bytearray, array.array, memoryview, collections.deque)
# 2-2.불변(tuple,str, bytes)

# 3. 리스트 및 튜플 고급

# Tuple advanced
# unpacking

# b,a=a,b
print(divmod(100, 9))
print(divmod(*(100, 9)))

print(*(divmod(100, 9)))

x, y, *rest = range(10)

print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable (가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))
l = l * 2
m = m * 2

print(l, id(l))  # --> id값이 다름
print(m, id(m))  # --> id값이 다름

l *= 2
m *= 2
print(l, id(l))  # --> id값이 다름
print(m, id(m))  # --> id값이 같음
# tuple로 계속 할당을 하면 메모리를 계속 가져다가 쓰겠다 id재할당이 계속 일어남
# list는 연산자의 활용에 따라 id 할당이 바뀜
print()
print()

# sort vs sorted
# 둘다 정렬하지만 다르다
# reverse, key= Len , key= str.Lower, key = func ... <-이런 옵션들이 있다

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted(r) -', sorted(f_list, reverse=True))
print('sorted(len) -', sorted(f_list, key=len))
print('sorted(end char) -', sorted(f_list, key=lambda x: x[-1]))
print('sorted(end char r) -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('original-', f_list)

# sort : 정렬 후 객체 직접 변경
print('---------------')
# 반환값 확인 (None)
print('sort- ', f_list.sort(), f_list)
print('sort- ', f_list.sort(reverse=True), f_list)
print('sort- ', f_list.sort(key=len), f_list)
print('sort- ', f_list.sort(key=lambda x:x[-1]), f_list)
print('sort- ', f_list.sort(key=lambda x:x[-1],reverse=True), f_list)


# List vs Array 에 적합한 사용법 설명
# 리스트기반 : 융통성, 자양한 자료형 ,범용적사용
# 숫자기반 : 배열(리스트와 거의 호환)