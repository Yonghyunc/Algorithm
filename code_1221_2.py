# 1221. [S/W 문제해결 기본] 5일차 - GNS
# 8/12


t = int(input())

for _ in range(1, t + 1):

    test_case, num = map(str, input().split())
    print(test_case)

    words = list(input().split())

    num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in num_str:
        # 문자열 개수 세기
        cnt = words.count(i)
        # 개수만큼 출력
        # 문자 사이 띄어쓰기 넣어줌
        print((i + ' ') * cnt, end=' ')
