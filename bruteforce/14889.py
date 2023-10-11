# 스타트와 링크
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
checked = [False for _ in range(N)]
answer = 1e9

def solve(cnt, idx):
    global answer
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if checked[i] and checked[j]:
                    start += S[i][j]
                elif not checked[i] and not checked[j]:
                    link += S[i][j]
        answer = min(answer, abs(start - link))
        return
    for i in range(idx, N):
        if not checked[i]:
            checked[i] = True
            solve(cnt+1, idx+1)
            checked[i] = False

solve(0, 0)
print(answer)