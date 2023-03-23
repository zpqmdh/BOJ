# 카드2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
L = [i for i in range(N, 0, -1)]
Q = deque(L)

while len(Q) > 1:
    Q.pop() # 제일 위에 있는 카드 바닥에 버리기
    card = Q.pop() # 제일 위에 있는 카드를
    Q.appendleft(card) # 가장 아래에 있는 카드 밑으로
print(Q[0])