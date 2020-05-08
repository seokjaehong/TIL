#20200507
def solution(a, b):
    months_cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    sum_ = sum([x for x in months_cal[:a - 1]]) + b
    a = sum_ % len(days)
    answer = days[a - 1]
    return answer
