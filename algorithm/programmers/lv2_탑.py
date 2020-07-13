# 내풀이
## answer를 미리 [0] * len(heights) 만큼 선언해놓으면 키에러 나는 걸 막을수 있겠다 
def solution(heights):
    answer=[]
    for i in range(len(heights)):
        for x in reversed(range(i)):
            if heights[i]<heights[x]:
                answer.append(x+1)
                break
        else:
            answer+=[0]
    return answer


# 다른사람들의 풀이
def solution(heights):
    answer = [0]*len(heights)
    stack = [] 

    for i in reversed(range(len(heights))):
        while stack and stack[-1][1] < heights[i]:
            idx, height = stack.pop()
            answer[idx] = i+1
        stack.append((i, heights[i]))

    return answer