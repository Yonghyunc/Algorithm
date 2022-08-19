# 3499. 퍼펙트 셔플

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    card = list(input().split())

    # n이 짝수일 때,
    if n % 2 == 0:
        left = card[:n//2]
        right = card[n//2:]

    # n이 홀수일 때,
    else:
        left = card[:n//2 + 1]
        right = card[n//2 + 1:]
        right.append("")        # 두 리스트의 길이를 맞춰줌

    # 테스트 케이스와 결과가 같은 줄에 나와야 함
    print(f'#{test_case}', end=' ')

    # 나눈 것들을 교대로 출력하게 함
    for i in range(len(left)):
        print(left[i], right[i], end=' ')

    # 다음 케이스와는 다른 줄에 나와야 함
    print()

