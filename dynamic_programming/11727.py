# 2×n 타일링 2
import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1
if N >= 2:
    dp[2] = 3

for i in range(3, N+1):
    if i % 2 == 0:
        dp[i] = (dp[i-1] * 2 + 1) % 10007
    else:
        dp[i] = (dp[i-1] * 2 - 1) % 10007

print(dp[N])