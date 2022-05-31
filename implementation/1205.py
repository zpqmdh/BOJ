# 등수 구하기
import sys
input = sys.stdin.readline
N, new, P = map(int, input().split())
if N == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    score.append(new)
    score.sort(reverse=True)
    rank = score.index(new) + 1
    if rank > P:
        print(-1)
    else:
        if N == P and new == score[-1]:
            print(-1)
        else:
            print(rank)