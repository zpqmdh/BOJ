# 기타 레슨
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = max(arr), sum(arr) # start: 가장 작은 블루레이 크기 / end: 가장 큰 블루레이 크기
while start<=end:
    mid = (start+end)//2
    cnt = 1
    tmp_value = 0
    for i in range(N):
        if tmp_value + arr[i] <= mid:
            tmp_value += arr[i]
        else:
            cnt += 1 # 새로운 블루레이 사용
            tmp_value = arr[i]
    if cnt > M: # 블루레이 크기를 늘려야 함 (= 개수 줄이기)
        start = mid + 1
    else: # 블루레이 크기를 줄여야 함 (= 개수 늘리기)
        end = mid - 1
print(start) # 최선의 값을 구해야 하기 때문
    
