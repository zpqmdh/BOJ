# 두 수의 합
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
X = int(input())

answer = 0
start, end = 0, N-1

while start<end:
    value = A[start]+A[end]
    if value == X:
        answer += 1
    if value >= X:
        end -= 1
    else:
        start += 1
print(answer)