# 숫자 카드 2
import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
M = int(input())
find_number = list(map(int, input().split()))
dict_card = {}
answer = []
for i in range(N):
    if dict_card.get(card[i]):
        dict_card[card[i]] += 1
    else:
        dict_card[card[i]] = 1
for key in find_number:
    if key in dict_card:
        answer.append(dict_card[key])
    else:
        answer.append(0)
    
print(*answer)