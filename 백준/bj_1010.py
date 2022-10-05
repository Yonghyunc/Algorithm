# 백준 1010. 다리 놓기


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = 1
    if n == m:
        print(ans)
    else:
        for i in range(m, m - n, -1):
            ans *= i
        for i in range(1, n + 1):
            ans //= i
        print(ans)