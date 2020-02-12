# prime_number
import time


def check_prime_part1(k):
    if k < 2:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


def check_prime_part2(k):
    if k < 2:
        return False
    if k == 2:
        return True

    if k % 2 == 0:
        return False
    for i in range(3, k, 2):
        if k % i == 0:
            return False
    return True


# 제곱근
def check_prime_part3(k):
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    l = round(k ** 0.5) + 1
    for i in range(3, l, 2):
        if k % i == 0:
            return False
    return True


# 에라토스테네스의체
def check_prime_part4(k):
    seive = [False, False] + [True] * (k - 1)
    for i, v in enumerate(seive):
        if v:
            j = i * 2
            while j <= k:
                seive[j] = False
                j += i
    return [x for (x, y) in enumerate(seive) if y]


# 에라토스테네스의체 + 파이썬 슬라이스 (리스트의 특정범위와 스텝범위를 통해 데이터 변경)
def check_prime_part5(k):
    seive = [False, False] + [True] * (k - 1)
    for n in range(2, int(k ** 0.5 + 1.5)):
        if seive[n]:
            seive[n * 2::n] = [False] * ((k - n) // n)
    return [x for x in range(k + 1) if seive[x]]


n = 30000

start_time = time.time()
a = [x for x in range(1, n) if check_prime_part1(x)]
time_diff = (time.time() - start_time)
print('#1-1 end', time_diff)

start_time = time.time()
b = [x for x in range(1, n) if check_prime_part2(x)]
time_diff = (time.time() - start_time)
print('#2-1 end', time_diff)

start_time = time.time()
c = [x for x in range(1, n) if check_prime_part3(x)]
time_diff = (time.time() - start_time)
print('#3-1 end', time_diff)

start_time = time.time()
d = check_prime_part4(n)
time_diff = (time.time() - start_time)
print('#4-1 end', time_diff)

start_time = time.time()
d = check_prime_part5(n)
time_diff = (time.time() - start_time)
print('#5-1 end', time_diff)
