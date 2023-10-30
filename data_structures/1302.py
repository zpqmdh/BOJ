# 베스트 셀러
import sys
input = sys.stdin.readline

N = int(input())
dict = {}
answer = []
for _ in range(N):
    name = input().strip()
    if name in dict.keys():
        dict[name] += 1
    else:
        dict[name] = 1
max_value = max(dict.values())
for k, v in dict.items():
    if v == max_value:
        answer.append(k)
answer.sort()
print(answer[0])