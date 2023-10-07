# 부분합
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
sum_value = 0
answer = 1e5

while left <= right:
    if sum_value >= S:
        answer = min(answer, right-left)
        sum_value -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum_value += arr[right]
        right += 1

if answer == 1e5:
    print(0)
else:
    print(answer)