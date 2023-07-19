# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = A[0]
if N > 1:
    dp[1] = A[0] + A[1]
if N > 2:
    dp[2] = max(dp[1], max(A[0]+A[2], A[1]+A[2]))
for i in range(3, N):
    dp[i] = max(dp[i-3]+A[i-1]+A[i], max(dp[i-2]+A[i], dp[i-1]))
print(max(dp))