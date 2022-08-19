# 1209. [S/W 문제해결 기본] 2일차 - Sum
# 8/10

for _ in range(10):
    t = int(input())
    arr = []
    for idx in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    sum_list = []  # 모든 합을 담을 리스트

    for i in range(100):
        sx = 0  # 각 행의 합
        sy = 0  # 각 열의 합
        for j in range(100):
            sx += arr[i][j]
            sy += arr[j][i]

        sum_list.append(sx)  # 총 100개
        sum_list.append(sy)  # 총 100개

    sd1 = 0  # 대각선1
    sd2 = 0  # 대각선2

    for i in range(100):
        sd1 += arr[i][i]
        sd2 += arr[99 - i][99 - i]

    sum_list.append(sd1)  # 1개
    sum_list.append(sd2)  # 1개

    # 최대값 구하기
    max_sum = sum_list[0]  # 초기 설정
    for i in range(202):
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]

    print(f'#{t} {max_sum}')
