# 1952. [모의 SW 역량테스트] 수영장

'''
[아이디어]
dfs 사용

costs[0] = 1일 이용권
costs[1] = 1달 이용권
costs[2] = 3달 이용권

'''


def dfs(idx, cost=0):
    global min_cost

    if idx == 12:                           # 12월까지 전부 확인
        if cost < min_cost:
            min_cost = cost
        return

    if not visited[idx]:
        # 1달 이용에 대한 금액
        if costs[0] * plans[idx] >= costs[1]:       # 1달권 이용
            cost += costs[1]
            visited[idx] = True
            dfs(idx + 1, cost)
            visited[idx] = False
            cost -= costs[1]
        else:                                       # 1일권 이용
            cost += costs[0] * plans[idx]
            visited[idx] = True
            dfs(idx + 1, cost)
            visited[idx] = False
            cost -= costs[0] * plans[idx]

        # 3달권 이용
        if idx <= 9:
            if not visited[idx + 1] and not visited[idx + 2]:
                cost += costs[2]
                visited[idx:idx + 3] = [True] * 3
                dfs(idx + 3, cost)
                visited[idx:idx + 3] = [False] * 3
                cost -= costs[2]


for tc in range(1, int(input()) + 1):
    costs = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    visited = [False] * 12

    min_cost = costs[-1]
    dfs(0)
    print(f'#{tc} {min_cost}')
