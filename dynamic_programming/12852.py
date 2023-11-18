# 1로 만들기 2
import sys
from collections import deque
input = sys.stdin.readline

X = int(input())
dp = [0 for _ in range(X+1)]
Q = deque()
Q.append([X, [X]])
while Q:
    cur, L = Q.popleft()
    if cur == 1:
        print(dp[1])
        print(*L)
        break
    if cur % 3 == 0 and not dp[cur//3]:
        dp[cur//3] = dp[cur] + 1
        Q.append([cur//3, L + [cur//3]])
    if cur % 2 == 0 and not dp[cur//2]:
        dp[cur//2] = dp[cur] + 1
        Q.append([cur//2, L + [cur//2]])
    if not dp[cur-1]:
        dp[cur-1] = dp[cur] + 1
        Q.append([cur-1, L + [cur-1]])
