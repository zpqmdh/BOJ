# 문자열
import sys
input = sys.stdin.readline

A, B = input().split()
answer = 50

def cal_diff(a, b): # 두 문자열의 차이 구하는 함수
    global answer
    dif = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dif += 1
    answer = min(answer, dif)
    return answer


if len(A) == len(B):
    cal_diff(A, B)
else:
    for i in range(len(B)-len(A)+1):
        cal_diff(A, B[i:i+len(A)])

print(answer)