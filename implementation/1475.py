# 방번호
import sys
input = sys.stdin.readline

N = input().strip()
cnt = [0 for _ in range(10)]
for n in N:
    idx = ord(n) - ord('0')
    if idx == 6 or idx == 9: # 6 or 9
        if cnt[6] > cnt[9]:
            cnt[9] += 1
        else:
            cnt[6] += 1
    else:
        cnt[idx] += 1
print(max(cnt))