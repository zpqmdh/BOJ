# 골드바흐의 추측
import sys
input = sys.stdin.readline
def Check_prime(N:int):
    prime = [1 for _ in range(N+1)]
    # 1: prime, 0: non-prime
    prime[1] = 0 # 1 is not prime
    for i in range(2, N+1):
        if prime[i] == 0: continue
        for j in range(i*2, N+1, i):
            prime[j] = 0
    return prime

def Goldbach(N:int):
    for i in range(1, N):
        if prime[i] == 1 and prime[N-i] == 1:
            print(N, "=", i, "+", N - i)
            return 1
        else:
            continue
    return 0


prime = Check_prime(1000000)
while True:
    N = int(input())
    if N == 0:
        break
    if Goldbach(N) == 1:
        continue
    else:
        print("Goldbach\'s conjecture is wrong.")