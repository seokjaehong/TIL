#20200507

def solution(arr):
    answer = []
    temp=10
    for a in arr:
        if temp!=a:
            answer.append(a)
            temp=a
    return answer