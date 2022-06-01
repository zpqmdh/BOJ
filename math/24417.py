# 알고리즘 수업 - 피보나치 수 2
MOD = 1000000007
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

n = int(input())
print(fibonacci(n)[0][1], n-2)