# 쉽게 푸는 문제
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
arr = [0]
idx = 1
ans = 0
while len(arr) <= B:
    for i in range(idx):
        arr.append(idx)
    idx += 1
for i in range(A, B+1):
    ans += arr[i]
print(ans)