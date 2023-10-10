# 차이를 최대로
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
l = []
answer = -1e9

def solve(cnt):
    global answer
    if cnt == N:
        total = 0
        for i in range(cnt-1):
            total += abs(l[i]-l[i+1])
        answer = max(answer, total)
        return
    for i in range(N):
        if arr[i] not in l:
            l.append(arr[i])
            solve(cnt+1)
            l.pop()

solve(0)
print(answer)
