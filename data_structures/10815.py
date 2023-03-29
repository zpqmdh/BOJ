# 숫자 카드
import sys
input = sys.stdin.readline
N = int(input())
card = set(list(map(int, input().split())))
M = int(input())
find = list(map(int, input().split()))
answer = []
for idx in range(len(find)):
    if find[idx] in card:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)