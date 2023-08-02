# 가장 긴 증가하는 부분 수열 4
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
answer = []

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]: # 증가
            dp[i] = max(dp[i], dp[j]+1)

max_value = max(dp)
max_idx = dp.index(max_value)
tmp = max_value

for i in range(max_idx, -1, -1):
    if dp[i] == tmp:
        answer.append(A[i])
        tmp -= 1

print(max_value)
for a in answer[::-1]:
    print(a, end=' ')

