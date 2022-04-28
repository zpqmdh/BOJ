# 비밀번호 찾기
N, M = map(int, input().split())
memo = {}
for i in range(N):
    site, passwd = input().split()
    memo[site] = passwd
for j in range(M):
    site = input()
    if site in memo:
        print(memo[site])