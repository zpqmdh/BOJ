# 이전 순열
import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    if L[i-1] > L[i]: # 앞자리 수가 더 클 때
        for j in range(N-1, 0, -1):
            if L[i-1] > L[j]:
                L[i-1], L[j] = L[j], L[i-1]
                L = L[:i] + sorted(L[i:], reverse=True)
                print(*L)
                exit(0)
print(-1)
