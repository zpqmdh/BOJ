# 오르막 수
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)] # dp[i][j]: i로 시작하면서 길이가 j인 오르막 수

for i in range(10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(9, -1, -1):
        dp[i][j] = sum(dp[i-1][j:]) % 10007
print(sum(dp[N]) % 10007)