# 백준 10872. 팩토리얼

import sys
input = sys.stdin.readline

n = int(input())
ans = 1
k = 1
while k <= n:
    ans *= k
    k += 1
print(ans)