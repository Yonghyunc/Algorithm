# 1206. [S/W 문제해결 기본] 1일차 - View


for test_case in range(1, 11):

    # 테스트케이스 길이
    t = int(input())

    # 테스트케이스
    floors = list(map(int, input().split()))

    # 조망권이 확보된 세대의 수
    view = 0

    # 양 옆 2칸을 비교하기 위해 요소가 5개씩 든 리스트 생성
    for i in range(2, len(floors) - 2):
        five_list = floors[i - 2 : i + 3]

        # 만약 i번째 수가 양 옆 2칸씩보다 크다면 그 차를 구함
        if floors[i] == max(five_list):
            minus = []
            for j in five_list:
                minus.append(floors[i] - j)

            # 자기 자신을 뺀 수인 0이 무조건 존재
            minus.remove(0)

            # 차 중 가장 작은 수가 조망권을 가진 세대의 수
            view += min(minus)

    print(f'#{test_case} {view}')
