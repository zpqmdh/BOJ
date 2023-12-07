# 풍선 터뜨리기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
Q = deque() 
for i in range(1, N+1):
    Q.append((i, nums[i-1]))
answer = []
while Q:
    idx, value = Q.popleft()
    answer.append(idx)
    if value > 0: # 오른쪽으로
        while Q and value > 1:
            Q.append(Q.popleft())
            value -= 1
    else: # 왼쪽으로
        while Q and value < 0:
            Q.appendleft(Q.pop())
            value += 1
print(*answer)