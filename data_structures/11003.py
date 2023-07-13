# 최솟값 찾기
import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
D = [0 for _ in range(N)]
Q = deque()
for i in range(N):
    # step1: A[i]보다 더 큰 값이 덱에 있다면, 최솟값의 가능성이 없기 때문에 pop
    while Q and Q[-1][1] > A[i]:
            Q.pop()
    # step2: 덱에 A[i] 추가
    Q.append([i, A[i]])
    # step3: window size를 벗어나면 popleft
    if Q[0][0] <= i-L:
        Q.popleft()
    print(Q[0][1], end=' ')
