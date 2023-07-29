# LCS
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

length1, length2 = len(str1), len(str2)

dp = [[0 for _ in range(length2+1)] for _ in range(length1+1)]
for i in range(1, length1+1):
    for j in range(1, length2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
print(dp)