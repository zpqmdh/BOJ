# 물통
import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
answer = []
Q = deque()
Q.append((0, 0, C))
visited = [[[False for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]
while Q:
    a, b, c = Q.popleft()
    if visited[a][b][c] == True:
        continue
    visited[a][b][c] = True
    if a == 0:
        answer.append(c)
    # a->b
    if a+b > B:
        Q.append((a+b-B, B, c))
    else:
        Q.append((0, a+b, c))
    # a->c
    if a+c > C:
        Q.append((a+c-C, b, C))
    else:
        Q.append((0, b, a+c))
    # b->a
    if b+a > A:
        Q.append((A, b+a-A, c))
    else:
        Q.append((b+a, 0, c))
    # b->c
    if b+c > C:
        Q.append((a, b+c-C, C))
    else:
        Q.append((a, 0, b+c))
    # c->a
    if c+a > A:
        Q.append((A, b, c+a-A))
    else:
        Q.append((c+a, b, 0))
    # c->b
    if c+b > B:
        Q.append((a, B, c+b-B))
    else:
        Q.append((a, c+b, 0))
    
answer.sort()
for i in range(len(answer)):
    print(answer[i], end=' ')