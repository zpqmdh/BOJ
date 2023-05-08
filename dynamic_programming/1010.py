# 다리 놓기
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    value = 1
    for i in range(N):
        value *= M-i
        value /= 1+i
    print(int(value))
