# 평범한 배낭
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
bag = [[0, 0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    bag.append(list(map(int, input().split())))
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]
        if j < weight: 
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[N][K])