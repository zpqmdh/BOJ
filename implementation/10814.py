# 나이순 정렬
import sys
input = sys.stdin.readline
N = int(input())
member = []
for _ in range(N):
    age, name = map(str, input().split())
    member.append((int(age), name))
member.sort(key = lambda x : x[0])
for i in member:
    print(i[0], i[1])