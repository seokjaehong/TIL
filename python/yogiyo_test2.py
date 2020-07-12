# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# S = '13 DUP 4 POP 5 DUP + DUP + -'
# S='5 6 + -'
# S = '3 DUP 5 - -'
S = '3 3 3 3 DUP DUP DUP 5 - -'
S = 'POP'


def solution(S):
    s = S.split(" ")
    result = []
    for i in s:

        # print("****", i)
        if i.isdigit():
            result += [i]
        elif i == 'DUP':
            try:
                a = result[-1]
            except IndexError:
                return -1
            result += [a]
        elif i == 'POP':
            try:
                result.pop(len(result) - 1)
            except:
                return -1
        elif i == "+":
            try:
                a = result.pop(len(result) - 1)
                b = result.pop(len(result) - 1)
            except IndexError:
                return -1
            result += [str(int(a) + int(b))]
        elif i == "-":
            try:
                a = result.pop(len(result) - 1)
                b = result.pop(len(result) - 1)
            except IndexError:
                return -1
            result += [str(int(a) - int(b))]
        else:
            pass
    return int(result[-1])


if __name__ == "__main__":
    a = solution(S)
    print(a)
