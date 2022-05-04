# ATM
import sys
N = int(sys.stdin.readline())
person = list(map(int, sys.stdin.readline().split()))
atm = [0 for _ in range(N)]
for i in range(N):
    atm[i] = [i, person[i]]
atm.sort(key=lambda x : x[1])
ans = 0
for i in range(N):
    ans += atm[i][1] * (N-i)
print(ans)