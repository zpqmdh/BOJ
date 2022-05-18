# 피보나치 수 3
'''
참고) https://janghw.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Divide-and-Conquer-%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5
'''
MOD = 1000000
def multiply(a, b):
    matrix = [[0 for _ in range(2)] for _ in range(2)]
    matrix[0][0] = (a[0][0] * b[0][0] % MOD + a[0][1] * b[1][0] % MOD) % MOD
    matrix[1][0] = (a[0][0] * b[0][1] % MOD + a[0][1] * b[1][1] % MOD) % MOD
    matrix[0][1] = (a[1][0] * b[0][0] % MOD + a[1][1] * b[1][0] % MOD) % MOD
    matrix[1][1] = (a[1][0] * b[0][1] % MOD + a[1][1] * b[1][1] % MOD) % MOD
    return matrix
def fibonacci(n):
    if n == 1:
        matrix = [[1, 1], [1, 0]]
        return matrix
    tmp = fibonacci(n//2)
    if n % 2 == 0:
        return multiply(tmp, tmp)
    else:
        return multiply(multiply(tmp, tmp), fibonacci(1))

N = int(input())
print(fibonacci(N)[0][1])