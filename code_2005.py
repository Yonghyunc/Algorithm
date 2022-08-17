# 2005. 파스칼의 삼각형
# 8/17

t = int(input())


for test_case in range(1, t + 1):
    n = int(input())
    print(f'#{test_case}')

    # 삼각형의 숫자를 담을 이중 리스트
    tri = [[1] for n in range(10)]
    # 두번째 줄은 미리 작성
    tri[1] = [1, 1]

    # 세번째 줄부터 삼각형 채우기
    if n > 2:
        for i in range(2, n):
            for j in range(i - 1):
                bet = tri[i - 1][j] + tri[i - 1][j + 1]
                tri[i].append(bet)
            tri[i].append(1)

    for i in range(n):
        print(*tri[i])
