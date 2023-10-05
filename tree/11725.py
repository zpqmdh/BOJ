# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = {}
for i in range(1,N+1):
	tree[i] = []
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def solve():
    Q = deque([1])
    parent = [0] * (N+1)
    while Q:
        cur = Q.popleft()
        for i in tree[cur]:
            if parent[i] == 0 and i != 1:
                parent[i] = cur
                Q.append(i)
    for i in range(2, N+1):
        print(parent[i])

solve()