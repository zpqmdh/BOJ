# 오큰수
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
comp = deque()
answer = [0 for _ in range(N)]

for i in range(N-1, -1, -1):
    while comp and A[i] >= comp[0]:
        comp.popleft()
    if comp:
        answer[i] = str(comp[0])
    else:
        answer[i] = '-1'
    comp.appendleft(A[i])

print(' '.join(answer))