# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])
            
print(max(dp))