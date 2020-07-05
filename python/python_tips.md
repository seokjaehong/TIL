## 몫과 나머지 
```python3
a = 7
b = 5
print(a//b, a%b)
```
- 일반적으로 몫과 나머지는 (1)위와 같이 산출한다. 
- Python에는 (2)`divmod` 기능이 있다. 작은숫자를 다룰때는 (1)이 더 빠르고, 큰숫자를 다룰때는 (2)가 더 빠르다. 

## 진법변환 
 - python의 int함수는 진법변환 `int(x, base=10)` 이 가능함 
```
num = '3212'
base = 5
answer = int(num, base)
```

### 문자열 정렬 
파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.
```
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```
### 알파벳 출력

```
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```

### zip.1 
여러개의 List를 동시에 순회 

```python3
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )
```

### zip.2 
- key,value로 이루어진 dict 생성 

```
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

### 모든 멤버의 type 변환하기 - map

```
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```

### 곱집합 (Cartesian product)

```
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
>>
[('A', 'x', '1'),
 ('A', 'x', '2'),
 ('A', 'x', '3'),
 ('A', 'x', '4'),
 ...
 ('D', 'x', '4'),
 ('D', 'y', '1'),
 ('D', 'y', '2'),
 ('D', 'y', '3'),
 ('D', 'y', '4')]
```

### 2차원 리스트를 1차원으로 

```
# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))
```

### 순열, 조합 

```
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```

### 많이등장하는 알파벳 찾기

```
temp={}
for i,v in enumerate(list(set(my_str))):
    temp[v]=my_str.count(v)
print("".join(sorted(x for x in temp.keys() if temp[x]==max(temp.values()))))
```

### 특정 List에 대한 logic넣기 (feat.lambda)

list(map(lambda x: len(x), mylist))