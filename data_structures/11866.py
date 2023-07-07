# 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
Q = deque()
for i in range(1, N+1):
    Q.append(i)
cnt = 1
answer = []
while Q:
    value = Q.popleft()
    if cnt == K:
        answer.append(value)
        cnt = 1
    else:
        Q.append(value)
        cnt += 1
for i in range(len(answer)):
    if i == 0:
        print("<", end='')
    else:
        print(", ", end='')
    print(answer[i], end='')
print(">")