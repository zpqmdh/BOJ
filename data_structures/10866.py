# 덱
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
deq = deque()
while N:
    cmd = input().split()
    if cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    N -= 1