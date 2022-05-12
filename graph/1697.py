# 숨바꼭질
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
pos = [0 for _ in range(100001)]
dx = [1, -1]
def bfs():
    Q = deque([])
    Q.append(N)

    while Q:
        x = Q.popleft()

        if x == K:
            print(pos[x])
            return

        for i in range(3):
            if i == 2:
                nx = x * 2
            else:
                nx = x + dx[i]

            if is_possible(nx) == True and pos[nx] == 0:
                pos[nx] = pos[x] + 1
                Q.append(nx)
    
def is_possible(x):
    if x<0 or x>100000:
        return False
    return True
bfs()
