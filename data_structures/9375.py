# 패션왕 신해빈
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    wear = []
    kind = {}
    for i in range(N):
        a, b = sys.stdin.readline().split()
        wear.append([a, b])
        if wear[i][1] not in kind:
            kind[wear[i][1]] = 1
        else:
            kind[wear[i][1]] += 1
    ans = 1
    keys = list(kind)
    for i in range(len(keys)):
        ans *= kind[keys[i]] + 1

    print(ans - 1)