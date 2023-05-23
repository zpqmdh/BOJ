# 랜선 자르기
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
arr.sort()
start, end = 1, arr[-1]
while start <= end:
    mid = (start+end)//2
    res = 0
    for i in arr:
        res += i//mid
    if res >= N: start = mid + 1
    else: end = mid - 1
print(end)