# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
# 8/18

# 노드의 연결 여부를 파악하는 함수
def dfs(s, g):
    visited[s] = True

    for next in graph[s]:
        if not visited[next]:
            dfs(next, g)

    # 두 노드가 연결되어 있다면 (s 노드부터 길을 찾아가다가 g 노드가 나오면)
    if visited[g] == True:
        global yes
        yes = 1


t = int(input())
for test_case in range(1, t + 1):
    v, e = map(int, input().split())

    # 각 노드에 직접 연결된 노드를 저장하기 위한 리스트
    graph = [[] for _ in range(v + 1)]

    # 연결 여부
    yes = 0

    # 경로 찾기에 사용할 리스트
    visited = [False] * (v + 1)

    # 각 노드에 직접 연결된 노드를 저장
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 경로의 존재를 확인할 출발 노드, 도착 노드
    s, g = map(int, input().split())

    # 두 노드가 직접 연결 되어있을 때,
    if g in graph[s]:
        yes = 1
    # 직접 연결 되어있지 않을때,
    else:
        dfs(s, g)

    print(f'#{test_case} {yes}')
