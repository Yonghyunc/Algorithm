# 1970. 쉬운 거스름돈

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    money_cnt = []

    # 큰 금액의 돈부터 고려
    for m in money:
        cnt = 0
        # 거슬러 줄 금액 n이 각 돈보다 크거나 같으면 계속해서,
        while n >= m:
            n = n - m       # 거스름돈에서 m의 값을 빼줌
            cnt += 1        # 사용한 돈의 개수는 계속해서 추가해줌
        money_cnt.append(cnt)

    print(f'#{test_case}')
    print(*money_cnt)

    '''
    출력 형식
    #1
    0 3 0 2 1 3 1 0
    '''
    # 프린트를 한번만 쓰는 방법은 없을까?

    # format => 동적 변화 적용 어려움
    # print('#{}\n{} {} {} {} {} {} {} {}'.format(test_case, *money_cnt))

    # 문자열로 변환하고 띄어쓰기 포함하여 join 후 출력
    # print(f'#{test_case}\n{" ".join(map(str, money_cnt))}')
