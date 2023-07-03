# 쿼드트리
import sys
input = sys.stdin.readline

def solve(y, x, N):
    color = MAP[y][x]
    for r in range(y, y+N):
        for c in range(x, x+N):
            if color != MAP[r][c]:
                color = -1
                break
    if color == -1:
        print("(", end='')
        solve(y, x, N//2)
        solve(y, x+N//2, N//2)
        solve(y+N//2, x, N//2)
        solve(y+N//2, x+N//2, N//2)
        print(")", end='')
    elif color == '0':
        print(0, end='')
    else:
        print(1, end='')

N = int(input())
MAP = [input().rstrip() for _ in range(N)]

result = []

solve(0, 0, N)
print(''.join(result))
