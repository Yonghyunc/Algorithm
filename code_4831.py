# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
# 8/9


# 노선 수
t = int(input())

for test_case in range(1, t + 1):

    # 최대 이동거리, 종점, 충전기 수
    k, n, m = map(int, input().split())

    # 정류장
    stop = list(map(int, input().split()))

    # 출발지 추가
    stop.insert(0, 0)

    # 목적지 추가
    stop.append(n)

    # 충전 횟수
    char_list = [0] * (m + 2)

    # 종점에 도착할 수 없는 경우
    for i in range(len(stop) - 1):

        if stop[i + 1] - stop[i] > k:
            char_num = 0
            break

    # else:
    #     # 지나쳐도 되는 충전소 개수 소거
    #     for i in range(len(stop) - 2):

    #         for j in range(k):
    #             if (stop[i + k] - stop[i] <= k) and (char_list[i] == 0):
    #                 char_list[i + 1] = 1

    #     char_num = m - char_list.count(1)

    else:
        pass

    print(f'#{test_case} {char_num}')
