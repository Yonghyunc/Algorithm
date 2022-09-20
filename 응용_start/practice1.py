# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기

for tc in range(1, int(input()) + 1):
    arr = input()

    for i in range(0, len(arr), 7):
        seven = arr[i:i + 7]
        val = 0
        for j in range(7):
            if seven[j] == '1':
                val += 2 ** (6 - j)
        print(val, end=' ')
    print()


'''
# input
2
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111
'''

'''
# output
1 13
0 120 12 7 76 24 60 121 124 103
'''