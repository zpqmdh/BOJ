# 색종이
import sys
input = sys.stdin.readline

square = [[0 for _ in range(100)] for _ in range(100)]
T = int(input())
res = 0

for _ in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if square[i][j] == 0:
                res += 1
            square[i][j] = 1
print(res)