# 시리얼 번호
import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
def sum_num(word):
    res = 0
    for i in word:
        if '0' <= i <= '9':
            res += int(i)
    return res
words.sort(key = lambda x:(len(x), sum_num(x), x))

for w in words:
    print(w)