# 피보나치 수 5

def fibo(n):
    # 1. 종료 조건 (Base case)
    if n <= 1:
        return n

    # 2. 점화식 (재귀식)
    return fibo(n - 1) + fibo(n - 2)


print(fibo(int(input())))