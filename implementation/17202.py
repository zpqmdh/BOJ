# 핸드폰 번호 궁합
import sys
input = sys.stdin.readline

P1 = input().strip()
P2 = input().strip()

dp = []
for i in range(len(P1)):
    dp.append(int(P1[i]))
    dp.append(int(P2[i]))
while len(dp)>2:
    for i in range(len(dp)-1):
        dp[i] = (dp[i] + dp[i+1]) % 10
    dp.pop()
print(*dp, sep='')