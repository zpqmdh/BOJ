# 통계학
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

dict = {}
for i in range(N):
    try:
        dict[A[i]] += 1
    except:
        dict[A[i]] = 1

A.sort() # 정렬

print(round(sum(A) / N)) # 산술평균
print(A[N//2]) # 중앙값

max_value = max(list(dict.values()))
value = []
for k, v in dict.items():
    if v == max_value:
        value.append(k)
value.sort()
# 최빈값
if len(value) > 1:
    print(value[1])
else:
    print(value[0])

print(A[-1] - A[0]) # 범위