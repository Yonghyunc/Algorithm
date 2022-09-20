# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔

import sys
sys.stdin = open('sample_input.txt')

def Bbit(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


# 암호코드의 비율
ratio = [
    [2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1],
    [1, 3, 2], [2, 3, 1], [1, 1, 4], [3, 1, 2],
    [2, 1, 3], [1, 1, 2]
]

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input()[:m] for _ in range(n)]

    # 1. 16진수 배열만 빼내기
    hexa_list = []
    hexa = ''
    for i in range(n):
        hexa = ''
        for j in range(m):
            if arr[i][j:j+2] != '00':
                hexa += arr[i][j]
            else:
                if hexa:
                    if hexa not in hexa_list:
                        hexa_list.append(hexa)
                hexa = ''

    # 2. 16진수 -> 10진수 -> 2진수
    binary_list = []
    binary = ''
    for hexa in hexa_list:
        for i in range(len(hexa)):
            num = int(hexa[i], 16)
            binary += Bbit(num)
        binary_list.append(binary)
        binary = ''

    result = 0

    # 3. 암호코드 찾기
    for binary in binary_list:
        # print(binary)
        code = []
        bin_ratio = [0, 0, 0]
        for i in range(len(binary)):
            if binary[i] == '1':
                if bin_ratio[1] == 0:           # 첫 번째 1 비율
                    bin_ratio[0] += 1
                else:                           # 세 번째 1 비율
                    bin_ratio[2] += 1

            elif bin_ratio[0] != 0 and binary[i] == '0':    # 가운데 0 비율
                if bin_ratio[2] != 0:                       # 비율 전부 채웠으면
                    bin_ratio = list(map(lambda x: x // min(bin_ratio), bin_ratio))
                    if bin_ratio in ratio:
                        code.append(ratio.index(bin_ratio))
                    bin_ratio = [0, 0, 0]
                else:
                    bin_ratio[1] += 1
            # print(bin_ratio)
        else:
            if bin_ratio in ratio:                              # for 문 끝나고 마지막 값 넣어주기
                code.append(ratio.index(bin_ratio))
        # print(code)

        # 4. 암호코드가 올바른지 판단
        if (sum(code[0:7:2]) * 3 + sum(code[1:7:2]) + code[7]) % 10 == 0:
            result += sum(code)
        # print(result)

    print(f'#{tc} {result}')
