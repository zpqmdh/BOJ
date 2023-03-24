# 나무 자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = sorted(list(map(int, input().split())))

low =  0
high = tree[-1]
while True:
    result = 0
    mid = (low + high) // 2
    for h in tree:
        if h > mid:
            result += h - mid
    if result == M or low > high: 
        # M과 result가 같지 않은 경우도 고려
        print(mid)
        break
    elif result > M:
        low = mid + 1
    elif result < M:
        high = mid - 1
