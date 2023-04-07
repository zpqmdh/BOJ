# 좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
C = []
for _ in range(N):
    C.append(list(map(int, input().split())))

C.sort(key=lambda x:(x[1], x[0]))

for idx in range(N):
    print(*C[idx])