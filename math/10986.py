# 나머지 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
S = [0 for _ in range(N)]
cnt = [0 for _ in range(M)]

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1
    cnt[remainder] += 1

for i in range(M):
    # 조합
    if cnt[i] > 1:
        answer += (cnt[i] * (cnt[i]-1)) // 2

print(answer)