# 요세푸스 문제
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
Q = deque([i for i in range(1, N+1)])
answer = []

while Q:
    for i in range(1, K):
        Q.append(Q.popleft())
    answer.append(Q.popleft())

print('<', end='')
for a in answer[:-1]:
    print(a, ', ', end='', sep='')
print(answer[-1], '>', sep='')