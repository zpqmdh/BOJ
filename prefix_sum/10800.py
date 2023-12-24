# 컬러볼
import sys
input = sys.stdin.readline

N = int(input())
A = []
max_color = -1
for i in range(N):
    color, size = map(int, input().split())
    if max_color < color:
        max_color = color
    A.append((color, size, i))
A.sort(key = lambda x: x[1]) # 크기(오름차순) -> 색(오름차순) 정렬
C = [0 for _ in range(max_color+1)]
answer = [0 for _ in range(N)]

j = 0
tmp = 0

for i in range(1, N):
    while A[j][1] < A[i][1]:
        C[A[j][0]] += A[j][1] 
        tmp += A[j][1]
        j += 1
    answer[A[i][2]] = tmp - C[A[i][0]] # 크기가 작으면서 해당 공이랑 같은 색 공 빼기

for i in range(N):
    print(answer[i])
