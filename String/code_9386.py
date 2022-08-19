# 9386. 연속한 1의 개수
# 8/12

t = int(input())

for test_case in range(1, t + 1):

    # 수열의 길이
    sl = int(input())

    # 테스트케이스
    seq = input()

    # 0으로 문자열 분리
    seq_split = seq.split('0')

    max_count = 0

    # 분리한 문자열의 길이를 비교하여 가장 큰 값을 찾음
    for i in range(len(seq_split)):
        if max_count < len(seq_split[i]):
            max_count = len(seq_split[i])

    print(f'#{test_case} {max_count}')
