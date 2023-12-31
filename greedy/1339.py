# 단어 수학
import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
D = {}
for word in words:
    number = 1
    for w in range(len(word)-1, -1, -1):
        if word[w] not in D.keys():
            D[word[w]] = number
        else:
            D[word[w]] += number
        number *= 10

D_sort = sorted(D.values(), reverse=True)
value = 9
answer = 0
for v in D_sort:
    answer += v * value
    value -= 1
print(answer)
