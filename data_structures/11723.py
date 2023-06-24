# 집합
import sys
input = sys.stdin.readline

S = set()
M = int(input())

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'add':
        S.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        S.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.discard(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
    elif cmd[0] == 'all':
        S = set([i for i in range(1, 21)])
    elif cmd[0] == 'empty':
        S = set()