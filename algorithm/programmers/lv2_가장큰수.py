
## 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
## 0이 들어간 간경우 int('000') 처리를 해서 str(int(xxxxx))를 하면 예외처리를 안해도되겠다


```
def solution(numbers):
    dd=len(str(max(numbers)))
    numbers = list(map(str,numbers))
    a=sorted(numbers, key=lambda x: x*dd,reverse=True)
    d=''.join(str(x) for x in a)
    if d[0]=="0":
        return "0"
    return d
```