# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# 8/23

def factory(make, x):
    global cost
    global min_cost

    if cost > min_cost:     # 합산 비용이 최소 생산 비용을 넘으면 가지치기
        return

    if len(make) == n:      # n개의 제품을 모두 생산하였을 경우,
        if min_cost > cost:
            min_cost = cost
        return

    for y in range(n):
        if not visited[y]:
            visited[y] = True
            make.append(arr[x][y])
            cost += arr[x][y]

            factory(make, x + 1)

            visited[y] = False
            make.pop()
            cost -= arr[x][y]


for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n   # 생산 여부
    make = []               # 공장별 생산비용
    cost = 0                # 총 생산비용
    min_cost = 1000000      # 최소 생산비용
    factory([], 0)

    print(f'#{test_case} {min_cost}')