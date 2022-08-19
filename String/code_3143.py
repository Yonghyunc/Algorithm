# 3143. 가장 빠른 문자열 타이핑
# 8/16

t = int(input())

for test_case in range(1, t + 1):
    a, b = input().split()
    print(f'#{test_case} {len(a)- a.count(b)*(len(b) -1)}')

# a의 문자열 길이에서 (b문자열이 포함된 개수) x (b문자열의 길이 - 1)을 빼줌
