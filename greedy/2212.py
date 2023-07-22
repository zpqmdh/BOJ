# 센서
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
A = list(map(int, input().split()))
dist = []
A.sort()

for i in range(1, N):
    dist.append(A[i]-A[i-1])
dist.sort()

if K >= N:
    print(0)
else:
    for _ in range(K-1):
        dist.pop()
    print(sum(dist))
