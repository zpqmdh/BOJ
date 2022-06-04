# 단어 정렬
import sys
input = sys.stdin.readline
N = int(input())
word = []
for _ in range(N):
    word.append(input().rstrip())
word = set(word)
word = list(word)
word.sort(key = lambda x : (len(x), x))
for i in word:
    print(i)