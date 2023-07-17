# 수들의 합
import sys
input = sys.stdin.readline

S = int(input())
answer = 1
sum_value = 0
while True:
    sum_value += answer
    if sum_value > S:
        print(answer-1)
        break
    answer += 1
