# 회전하는 큐

# 풀이 1
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

# 풀이 2
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
Q = deque([i for i in range(1, N+1)])
res = []
idx = 0
cnt = 0
while True:
    if num == res:
        print(cnt)
        break
    cur = Q.popleft() # 1번 연산
    if num[idx] == cur:
        res.append(cur)
        idx += 1
    else:
        Q.appendleft(cur) # 1번 연산 원래대로
        if Q.index(num[idx]) < len(Q)/2: # 찾고자 하는 값이 큐의 앞쪽에 있을 때 -> 2번 연산이 효과적
            Q.append(Q.popleft())
            cnt += 1
        else: # 찾고자 하는 값이 큐의 뒤쪽에 있을 때 -> 3번 연산이 효과적
            Q.appendleft(Q.pop())
            cnt += 1