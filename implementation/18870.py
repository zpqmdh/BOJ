# 좌표 압축
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(X)
D = {}
value = 0
for idx in range(N):
    if sorted_X[idx] not in D.keys():
        D[sorted_X[idx]] = value
        value += 1
for x in X:
    print(D[x], end=' ')