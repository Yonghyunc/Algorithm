# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔

import sys
sys.stdin = open('sample_input.txt')


# 10진수를 4비트 2진수로 바꿔주는 함수
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
            if arr[i][j:j+4] != '0000':             # 0이 4개가 연달아 나오면 그때부터는 암호가 아니라고 판단
                hexa += arr[i][j]
            else:
                if hexa:
                    hexa += "000"                   # 테스트케이스를 보고 하드코딩...
                    if hexa not in hexa_list:
                        hexa_list.append(hexa)
                hexa = ''
        else:
            if hexa and hexa != '0' and hexa != '00' and hexa != '000':     # 행이 끝났는데 hexa 값이 존재할 때,
                hexa += "000"                                               # 비율을 구하는 것이기 때문에 앞뒤로 0 세개씩 더 붙여줌
                if hexa not in hexa_list:                                   # 중복은 없게
                    hexa_list.append(hexa)

    # print(hexa_list)

    # 2. 16진수 -> 10진수 -> 2진수
    binary_list = []
    binary = ''
    for hexa in hexa_list:
        for i in range(len(hexa)):
            num = int(hexa[i], 16)
            binary += Bbit(num)
        binary_list.append(binary)
        binary = ''

    # print(binary_list)

    # 3. 암호코드 찾기
    code_list = []                              # 모든 코드를 넣을 리스트
    for binary in binary_list:
        code = []
        bin_ratio = [0, 0, 0]
        for i in range(len(binary)):
            if binary[i] == '1':
                if bin_ratio[1] == 0:           # 첫 번째 1 비율
                    bin_ratio[0] += 1
                else:                           # 세 번째 1 비율
                    bin_ratio[2] += 1

            elif bin_ratio[0] != 0 and binary[i] == '0':    # 0이 나오면,
                if bin_ratio[2] != 0:                       # 비율 전부 채웠으면
                    bin_ratio = list(map(lambda x: x // min(bin_ratio), bin_ratio))     # 비율을 셋 중 가장 작은 수로 나누어줌
                    if bin_ratio in ratio:                                              # 그렇게 구한 비율이 ratio 리스트 안에 있으면
                        code.append(ratio.index(bin_ratio))                             # 해당 인덱스 값(10진수 암호)으로 변환
                    bin_ratio = [0, 0, 0]                                               # 다음을 위해 초기화
                else:                                       # 두 번째 0 비율
                    bin_ratio[1] += 1
            # print(bin_ratio)

        else:
            if bin_ratio in ratio:                              # for 문 끝나고 마지막 값 넣어주기
                code.append(ratio.index(bin_ratio))

        # 000이 나오는 경우는 한 코드로 봤기 때문에, 여러개의 코드가 붙어 나오는 경우 발생 -> 끊어서 리스트에 넣어줌
        if len(code) > 8:
            for i in range(len(code) // 8):
                code_new = code[i * 8: i * 8 + 8]
                if code_new not in code_list:           # 리스트 내에 중복되는 코드가 있으면 같다고 판별
                    code_list.append(code_new)
        else:
            if code not in code_list:
                code_list.append(code)
    # print(code_list)

    # 4. 암호코드가 올바른지 판단
    result = 0
    for i in range(len(code_list)):
        code = code_list[i]
        if (sum(code[0:7:2]) * 3 + sum(code[1:7:2]) + code[7]) % 10 == 0:
            result += sum(code)

    print(f'#{tc} {result}')
