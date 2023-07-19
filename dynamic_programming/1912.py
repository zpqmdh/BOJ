# 연속합
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [-1000 for _ in range(N)]

answer = A[0]
dp[0] = A[0]

for i in range(1, N):
    dp[i] = max(dp[i-1]+A[i],A[i])
    answer = max(answer, dp[i])

print(answer)
