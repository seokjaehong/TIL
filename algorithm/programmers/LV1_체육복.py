#20200507
def solution(n, lost, reserve):
    a=[1]*n
    for b in lost:
        a[b-1]-=1
    for c in reserve:
        a[c-1]+=1
    for idx,val in enumerate(a):
        if val==2:
            if idx-1>=0 and a[idx-1]==0:
                a[idx]-=1
                a[idx-1]+=1
            elif idx+1<=len(a)-1 and a[idx+1]==0:
                a[idx]-=1
                a[idx+1]+=1
            else:
                pass
    answer = len([x for x in a if x>=1])
    return answer