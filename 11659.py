# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = arr[0]
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[e]-dp[s-1])