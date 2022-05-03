# 회의실 배정
N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([b, a])
arr.sort()
ans = 1
end = arr[0][0]
for i in range(1, N):
    if arr[i][1] >= end:
        ans += 1
        end = arr[i][0]
print(ans)