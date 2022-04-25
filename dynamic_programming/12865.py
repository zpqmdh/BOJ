# DP
import sys
N, K = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    arr.append([w, v])
weight = 0
while weight <= K:
    