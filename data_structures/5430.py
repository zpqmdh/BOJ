# AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    N = int(input())
    L = input().strip()
    DQ = deque()
    Q = [] # DQ에 값을 넣기 위함 (L에서 숫자만 가져옴)
    for i in L:
        if i == '[' or i == ',' or i == ']':
            if Q: DQ.append(int(''.join(Q)))
            Q.clear()
        else:
            Q.append(i)
        
    flag = False # 앞에서부터
    error = False # 에러처리
    for c in p:
        if c == 'R':
            flag = not flag # 뒤에서부터 (뒤집기)
        elif c == 'D':
            if not DQ:
                error = True
                break
            if flag: DQ.pop()
            else: DQ.popleft()
    if error: print("error")
    else:
        if DQ:
            if flag:
                print('[',end='')
                for i in range(len(DQ)-1, -1, -1):
                    if i != 0:
                        print(DQ[i], end=',')
                    else:
                        print(DQ[i], end='')
                print(']')
            else:
                print('[',end='')
                for i in range(len(DQ)):
                    if i != len(DQ)-1:
                        print(DQ[i], end=',')
                    else:
                        print(DQ[i], end='')
                print(']')
        else:
            print('[]')