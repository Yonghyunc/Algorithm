# 1945. 간단한 소인수분해
# 8/9 extra


t = int(input())

for test_case in range(1, t + 1):
    num = int(input())

    pf = [2, 3, 5, 7, 11]  # 소수 리스트
    div_count = [0] * 5  # 소수 카운트 리스트

    for i, v in enumerate(pf):
        while num % v == 0:  # 더 이상 해당 소수로 나눌 수 없을 때까지
            div_count[i] += 1  # 나눌 때마다 카운트를 더해줌
            num = num // v  # 다음 반복은 소수로 나눈 수로 수행

    print(f'#{test_case}', end=' ')
    print(*(div_count))

    # print(f'#{test_case} *{div_count}')
