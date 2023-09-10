# 어린 왕자
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    answer = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        pr = r ** 2
        if pr > d1 and pr > d2:
            continue
        elif pr > d1:
            answer += 1
        elif pr > d2:
            answer += 1
    print(answer)

