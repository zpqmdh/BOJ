# 명령 프롬프트
import sys
input = sys.stdin.readline

N = int(input())
cmd = [list(input().rstrip()) for _ in range(N)]

for i in range(1, N):
    for j in range(len(cmd[0])):
        if cmd[0][j] != cmd[i][j]:
            cmd[0][j] = '?'
print(''.join(cmd[0]))