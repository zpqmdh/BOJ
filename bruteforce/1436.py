# 영화감독 숌
import sys
input = sys.stdin.readline
N = int(input())
number = []
flag = True
cur = 1
while flag:
    if str(cur).find('666') != -1:
        number.append(cur)
    cur += 1
    if len(number) >= N:
        flag = False

print(number[N-1])