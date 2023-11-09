# 예산
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

start, end = 1, max(A)
answer = 0
while start <= end:
    mid = (start + end) // 2 # 상한액
    tmp_max = 0 # 초기화
    for i in A:
        if i < mid: 
            tmp_max += i
        else:
            tmp_max += mid
    if tmp_max > M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
