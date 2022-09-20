# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자


# 10진수 -> 4비트 이진수
def Bbit(i):
    output = ""
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


for tc in range(1, int(input()) + 1):
    arr = input()

    binary = ''
    for i in range(len(arr)):
        # 16진수 -> 10진수
        num = int(arr[i], 16)
        # 10진수 -> 2진수
        binary += Bbit(num)

    # 7비트씩 묶어 10진수로 변환
    for i in range(0, len(binary), 7):
        # 마지막은 개수 상관없이 묶음
        if i + 7 > len(binary):
            seven = binary[i:]
        else:
            seven = binary[i:i + 7]

        val = 0
        for j in range(len(seven)):
            if seven[j] == '1':
                val += 2 ** (len(seven) - 1 - j)
        print(val, end=' ')
    print()



'''
# input
2
0F97A3
01D06079861D79F99F
'''

'''
# output
7 101 116 3
0 116 12 7 76 24 58 121 124 103 3
'''