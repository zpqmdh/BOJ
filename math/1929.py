# 소수 구하기
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
prime = [True for _ in range(N+1)]
prime[1] = False
for i in range(2, N+1):
    if prime[i]:
        for j in range(2*i, N+1, i):
            prime[j] = False
for i in range(M, N+1):
    if prime[i]:
        print(i)