# 1221. [S/W 문제해결 기본] 5일차 - GNS
# 8/12

# 딕셔너리, 버블정렬
# 실행시간 너무 긺!!!!

number = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9,
}

t = int(input())

for _ in range(1, t + 1):

    test_case, num = map(str, input().split())

    # 문자열 입력
    words = list(input().split())

    # 딕셔너리 value 이용해 오름차순 정렬
    for _ in range(int(num)):
        for i in range(int(num) - 1):
            if number[words[i]] > number[words[i + 1]]:
                words[i], words[i + 1] = words[i + 1], words[i]

    # print(test_case, *words, sep="\n")
    print(test_case)
    print(*words)
