# 1954. 달팽이 숫자
# 8/10

t = int(input())

for test_case in range(1, t + 1):

    n = int(input())

    di = [0, 1, 0, -1]  # i 인덱스 이동
    dj = [1, 0, -1, 0]  # j 인덱스 이동

    num = 1  # 출력할 숫자

    snail = [[0] * n for _ in range(n)]  # n*n의 빈 배열
    idx_i = 0  # 행 인덱스
    idx_j = 0  # 열 인덱스
    snail[0][0] = 1

    while True:
        for k in range(4):  # 델타 인덱스
            while True:

                # 델타 이동을 위한 조건문
                if 0 <= idx_i < n and 0 <= idx_j < n:
                    idx_i = idx_i + di[k]
                    idx_j = idx_j + dj[k]

                    # 이동한 값이 다음 조건을 충족시킬시 snail 인덱스에 숫자 입력
                    # 1. 행 인덱스와 열 인덱스가 모두 0에서 n-1이라는 범위 안에 위치할 것 (즉, snail 리스트의 인덱스 범위를 벗어나지 말 것)
                    # 2. 해당 인덱스의 값이 0일 것 (즉, 지나오지 않은 위치일 것)
                    if 0 <= idx_i < n and 0 <= idx_j < n and snail[idx_i][idx_j] == 0:
                        num += 1
                        snail[idx_i][idx_j] = num

                    # 위 조건을 만족하지 못할 시에는 인덱스 값을 델타 이동 이전으로 돌려놓고 다음 델타이동(di, dj)으로 넘어감
                    else:
                        idx_i = idx_i - di[k]
                        idx_j = idx_j - dj[k]
                        break

                else:
                    break

        # 마지막 숫자인 n*n이 나오면 while문을 종료
        if snail[idx_i][idx_j] == n * n:
            break

    # 테스트 케이스 번호 출력
    print(f'#{test_case}')

    # 리스트 언패킹하여 출력 -- 2차원 배열이라서 for문을 사용하였음
    for i in range(n):
        print(*snail[i])
