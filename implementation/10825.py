# 국영수
import sys
input = sys.stdin.readline
score = [] # 이름, 국어, 영어, 수학
N = int(input())
for _ in range(N):
    [name, ko, en, ma] = map(str, input().split())
    score.append([name, int(ko), int(en), int(ma)])
score.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(score[i][0])