# 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = sorted(list(map(int, input().split())))
        B = sorted(list(map(int, input().split())))
        answer = 0
        idx = 0
        for a in A:
            while True:
                if idx==M or a <= B[idx]:
                    answer += idx
                    break
                idx+=1
        print(answer)
if __name__ == '__main__':
    main()