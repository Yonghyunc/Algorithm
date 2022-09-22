# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

def cart(i):
    global val
    global min_val

    # 이미 최소 값을 넘어버렸으면, 그 경로로는 가지 않음
    if val > min_val:
        return

    for j in range(n):
        if arr[i][j] != 0 and not visited[j]:
            val += arr[i][j]
            visited[j] = True

            # 모든 구역을 방문하고 사무실로 돌아오면, 배터리 소비량 비교
            if j == 0 and visited == [True] * n:
                if val < min_val:
                    min_val = val

            # 연결되는 구역으로 이동하여 함수 실행
            cart(j)
            val -= arr[i][j]
            visited[j] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 각 구역을 한 번만 방문하기 위해, 방문 여부 표시
    visited = [False] * n

    val = 0
    min_val = 100 * 100
    cart(0)
    print(f'#{tc} {min_val}')