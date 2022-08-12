# 9367. 점점 커지는 당근의 개수
# 8/12


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    carrot = list(map(int, input().split()))

    # 기본 연속값
    cnt = 1

    # 연속값을 담을 리스트
    cnt_list = []

    for i in range(n - 1):

        # 연속값일 경우
        if carrot[i] + 1 == carrot[i + 1]:
            cnt += 1

        # 연속값이 아닐 경우, 연속값의 길이를 리스트에 담음
        else:
            cnt_list.append(cnt)
            cnt = 1  # 다시 초기화

    # 마지막 연속값을 리스트에 담음
    else:
        cnt_list.append(cnt)

    # 최대 연속값 구함
    max_cnt = 0

    for i in range(len(cnt_list)):
        if max_cnt < cnt_list[i]:
            max_cnt = cnt_list[i]

    print(f'#{test_case} {max_cnt}')
