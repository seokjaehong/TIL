###전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true
###[119, 97674223, 1195524421]	false
###[123,456,789]	true
def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i!=j and j.startswith(i):
                return False
    else:
        return True
