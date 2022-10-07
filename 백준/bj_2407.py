# 백준 2407. 조합

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
ans = 1
k = n

if m > n // 2:
    r = m
else:
    r = n - m

while k > r:
    ans *= k
    k -= 1

k = n
while k > r:
    ans //= (k - r)
    k -= 1

print(ans)