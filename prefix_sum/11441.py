# 합 구하기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] + [A[i] for i in range(N)]
for i in range(2, N+1):
    S[i] += S[i-1]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(S[b] - S[a-1])
