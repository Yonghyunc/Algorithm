'''
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다.
모든 정점을 너비우선탐색하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.

[입력]
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

[출력]
1 2 3 4 5 7 6
'''


def bfs(v):
    visited[v] = True
    queue = [v]
    print(v, end=' ')

    while queue:
        v = queue.pop(0)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                print(next_v, end=' ')


n, m = map(int, input().split())

edges = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]
    # 무방향
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)

bfs(1)
