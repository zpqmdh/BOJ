# 파도반 수열
import sys
input = sys.stdin.readline
T = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(T):
	N = int(input())
	if N > len(dp):
		for i in range(len(dp), N):
			dp.append(dp[i-2] + dp[i-3])
	print(dp[N-1])