# 공유기 설치
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input().strip()) for _ in range(N)]
A.sort()
start, end = 1, A[-1]-A[0] # start: 인접한 최소 거리, end: 인접한 최대 거리
while start <= end:
    mid = (start+end) // 2
    cnt = 1
    cur = A[0]
    for i in A[1:]:
        if cur + mid <= i:
            cnt += 1
            cur = i
    if cnt < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)

