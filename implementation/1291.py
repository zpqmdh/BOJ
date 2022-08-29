# 이면수와 임현수
import math
def prime_number(N): # 에라토스테네스의 체
    for i in range(2, N+1):
        if arr[i] == 0:
            continue
        primes.append(i)
        for j in range(2*i, N+1, i):
            arr[j] = 0
def get_div(N): # 소인수분해
    div = []
    i = 2
    while i <= N:
        if N % i != 0:
            i += 1
        else:
            div.append(i)
            N //= i
    return div
def sum_of_digit(N): # 각 자릿수의 합
    sum = 0
    for i in str(N):
        sum += int(i)
    if sum % 2 == 0:
        return False
    return True
def imyeonsu(N): # 이면수인가?
    if N >= 6 and sum_of_digit(N):
        return True
    return False
def imhyeonsu(N): # 임현수인가?
    if N == 2 or N == 4:
        return True
    if N > 1 and N not in primes: # 합성수
        if len(set(get_div(N))) % 2 == 0:
            return True
    return False

N = int(input())
arr = [i for i in range(N+1)]
primes = []

prime_number(N)

if imyeonsu(N) and imhyeonsu(N):
    print(4)
elif imyeonsu(N):
    print(1)
elif imhyeonsu(N):
    print(2)
elif not imyeonsu(N) and not imhyeonsu(N):
    print(3)