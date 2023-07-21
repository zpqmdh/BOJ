# 빗물
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = list(map(int, input().split()))
max_height = [0, A[0]]
answer = 0
for i in range(1, W-1):
    min_value = min(max_height[1], A[i+1])
    for j in range(max_height[0], i+1):
        if A[j] < min_value:
            answer += min_value - A[j]
            A[j] = min_value
    if max_height[1] < A[i]:
        max_height = [i, A[i]]
print(answer)
