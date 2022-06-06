# 퇴사
import sys
input = sys.stdin.readline
N = int(input())
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0] * (N+2)
for i in range(1, N+1):
    if i + arr[i][0] > N+1:
        dp[i+1] = max(dp[i+1], dp[i])
        continue
    dp[i+arr[i][0]] = max(dp[i+arr[i][0]], arr[i][1] + dp[i])
    dp[i+1] = max(dp[i+1], dp[i])
print(max(dp))