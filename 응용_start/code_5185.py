# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수


def Bbit(i):                                # 10진수를 4비트 2진수로 바꿔주는 함수
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


for tc in range(1, int(input()) + 1):
    n, hexa = input().split()
    arr = ''                                # 출력할 배열
    for i in range(int(n)):
        num = int(hexa[i], 16)              # 16진수 -> 10진수
        arr += Bbit(num)

    print(f'#{tc} {arr}')