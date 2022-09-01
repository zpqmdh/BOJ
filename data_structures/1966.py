# 프린터 큐
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    idx_Q = deque(list(range(N)))
    cnt = 0
    while Q:
        if Q[0] == max(Q):
            cnt += 1
            Q.popleft()
            if idx_Q.popleft() == M:
                print(cnt)
        else:
            # rotate(-1) == append(popleft())
            Q.rotate(-1)
            idx_Q.rotate(-1)