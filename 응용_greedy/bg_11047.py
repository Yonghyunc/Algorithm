# 백준 11047 : 동전 0
# while 문 사용 + 대소비교 후 뺄셈 반복 시 시간초과

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
result = 0

for i in range(n - 1, -1, -1):
    result += (k // coin[i])
    k %= coin[i]

print(result)