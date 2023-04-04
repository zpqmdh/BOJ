# 회전하는 큐
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))
answer = []
cnt = 0
Q = deque([i for i in range(1, N+1)])

while True:
    if answer == num:
        print(cnt)
        break
    idx = len(answer)
    while True:
        q = Q.popleft() # 1
        if q == num[idx]:
            answer.append(q)
            break
        else:
            Q.appendleft(q) # 원래대로
            if Q.index(num[idx]) < len(Q) / 2:
                Q.append(Q.popleft()) # 2
                cnt += 1
            else:
                Q.appendleft(Q.pop()) # 3
                cnt += 1
