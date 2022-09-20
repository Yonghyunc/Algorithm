# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오.
# 암호는 연속되어 있다.


# 10진수를 4비트 2진수로 바꾸는 함수
def Bbit(i):
    output = ""
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


# 암호비트패턴
secret = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

for tc in range(1, int(input()) + 1):
    arr = input()
    look = ''
    for i in range(len(arr)):
        num = int(arr[i], 16)
        look += Bbit(num)

    # 16진수를 2진수로 바꾼 문자 배열에서 암호비트패턴 찾기
    code = []
    j = len(look)
    while j >= 0:
        if look[j-6:j] in secret:
            code.insert(0, secret.index(look[j-6:j]))
            j -= 6
        else:
            j -= 1
    print(*code)



'''
# input
2
0DEC
0269FAC9A0
'''

'''
# output
0 2
1 1 7 8 0
'''