# 수열 정렬
import sys
input = sys.stdin.readline

# B[P[i]] = A[i]
# B: A를 오름차순으로 정렬한 것
# P: A가 몇번째로 작은지를 나타내는 것

N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = [0 for _ in range(N)]
visited = [False for _ in range(N)]

dic = {}
for i in range(N):
    dic[i] = A[i]

cnt = 0
for i in range(N):
    x = B[i]
    for j in dic.items(): # j = (idx, value)
        if j[1] == x and visited[j[0]] == False:
            P[j[0]] = cnt
            cnt += 1
            visited[j[0]] = True

print(*P)
