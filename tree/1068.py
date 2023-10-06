# 트리
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
delete = int(input())

tree = {}
for i in range(N):
	tree[i] = deque()
for i in range(N):
    value = parent[i]
    if i == delete:
        continue
    if value != -1: # 루트 노드가 아니면
        tree[value].append(i)

Q = deque([delete])
while Q:
    cur = Q.popleft()
    while tree[cur]:
        node = tree[cur].popleft()
        Q.append(node)
    del tree[cur]

answer = 0
for i in range(N):
    if i in tree and len(tree[i]) == 0:
        answer += 1
print(answer)
