# 2차원 배열의 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

dp[1][1] = arr[0][0]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

K = int(input())
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    print(dp[y2][x2] - dp[y2][x1-1] - dp[y1-1][x2] + dp[y1-1][x1-1])