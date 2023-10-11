# 외판원 순회 2
import sys
input = sys.stdin.readline

N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
answer = 1e7

def solve(cnt, start, cur, value):
    global answer
    if cnt == N-1:
        if w[cur][start] == 0: # 돌아갈 수 없음
            return
    if cnt == N:
        answer = min(answer, value+w[cur][start])
        return
    for i in range(N):
        if visited[i] == False and i != cur and w[cur][i] != 0:
            visited[i] = True
            solve(cnt+1, start, i, value+w[cur][i])
            visited[i] = False

solve(0, 0, 0, 0)
print(answer)