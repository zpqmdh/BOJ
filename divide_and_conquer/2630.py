# 색종이 만들기
import sys
input = sys.stdin.readline

def solve(y, x, N):
    color = paper[y][x]
    for r in range(y, y+N):
        for c in range(x, x+N):
            if color != paper[r][c]:
                solve(y, x, N//2)
                solve(y, x+N//2, N//2)
                solve(y+N//2, x, N//2)
                solve(y+N//2, x+N//2, N//2)
                return
    if color == 0:
        white.append('O')
    else:
        blue.append('O')

N = int(input())
paper = []

white = []
blue = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

solve(0, 0, N)
print(len(white))
print(len(blue))