# 10726. 이진수 표현
# 비트 연산

def Bbit(i, n):
    output = ""
    for j in range(n - 1, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    if Bbit(m, n) == '1' * n:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
