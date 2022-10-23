# 수열
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
day = list(map(int, input().split()))
res = []
res.append(sum(day[:K]))
for i in range(N-K):
	res.append(res[i]-day[i]+day[i+K])
print(max(res))