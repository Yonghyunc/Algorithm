# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

for tc in range(1, int(input()) + 1):
    n = int(input())        # 신청서
    # 종료 시간이 빠른 순서대로 정렬
    task = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

    end = task[0][1]        # 현재 종료 시간
    container = 1           # 작업량

    for i in range(1, n):
        if task[i][0] >= end:       # 시작 시간과 현재 종료 시간 비교
            container += 1          # 작업 + 1
            end = task[i][1]        # 현재 종료 시간 갱신
    print(f'#{tc} {container}')
