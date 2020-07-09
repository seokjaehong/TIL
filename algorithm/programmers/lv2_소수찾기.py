# 중복제거하는 부분 다시 작성해볼것 
# check_prime_number 부분에 체크 하는 로직 수정해서 깔끔하게 바꾸기.. 

from itertools import permutations
def check_prime_number(_num):
    if _num==2:
        return True

    if _num<=1 or _num%2==0:
        return False

    cnt=0
    for i in range(3,_num+1,2):
        if _num%i==0:
            cnt+=1
        if cnt>=2:
            return False
    return True

def solution(numbers):
    answer=0
    num_list =list(numbers)
    result=[]
    for i in range(1,len(numbers)+1):
        result+=[int(''.join(list(x))) for x in list(permutations(numbers,i))]
    cnt=0
    for x in list(set(result)):
        if check_prime_number(x):
            cnt+=1
    return cnt 



## 수정후 
from itertools import permutations

def check_prime_number(_num):
    #짝수는 일단거름, 1도 거름 
    if _num<=1 or _num%2==0:
        return False
    
    cnt=0
    #짝수는 이미 걸렀으니 홀수 중에서만 거름 
    for i in range(2,_num+1,2):
        if _num%i==0:
            cnt+=1
        if cnt>=2:
            return False
    return True

def solution(numbers):
    answer=0
    num_list =list(numbers)
    result=set()

    for i in range(1,len(numbers)+1):
        # result+=[int(''.join(list(x))) for x in list(permutations(numbers,i))]
        # 미리 set으로 선언해서 시간을 줄임 
        result |= set(map(int, map("".join, permutations(num_list, i))))
    
    cnt=0
    for x in result:
        if check_prime_number(x):
            cnt+=1
    return cnt

    #1. 조합가능한 숫자를 체크 
    #2. 해당 숫자가 소수인지 체크 
    #3. int형으로 전환 후 result 에 없으면 add (0인지 체크해야하니까)