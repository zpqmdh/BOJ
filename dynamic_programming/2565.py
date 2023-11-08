# 전깃줄
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if A[j][1] < A[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))