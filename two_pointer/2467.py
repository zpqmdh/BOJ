# 용액
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
result = 1e10
answer = []

while left < right:
    value = arr[left] + arr[right]
    if abs(value) < result:
        result = abs(value)
        answer = [arr[left], arr[right]]
    if value < 0:
        left += 1
    else:
        right -= 1
        
print(answer[0], answer[1], sep=' ')