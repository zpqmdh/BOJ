# 한수
N = int(input())
ans = 0
def f(N):
    global ans
    arr = str(N)
    dist = []
    for i in range(0, len(arr)-1):
        dist.append(int(arr[i]) - int(arr[i+1]))
    set_dist = set(dist)

    if len(set_dist) == 1:
        ans += 1

for i in range(1, N+1):
    if i < 100: # 두 자리수까지는 등차수열을 이룸
        ans += 1
    else:
        f(i)
print(ans)