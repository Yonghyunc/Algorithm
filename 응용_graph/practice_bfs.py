# 모든 정점을 너비 우선 탐색
# 시작 정점 = 1

'''
# input
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v):
    visited[v] = True
    queue = [v]
    print(v, end=' ')

    while queue:
        v = queue.pop(0)
        for k in graph[v]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)
                print(k, end=' ')


arr = list(map(int, input().split()))
n = len(arr) // 2
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)     # 방문 여부 확인

for i in range(n):              # 인접 리스트 생성
    graph[arr[i * 2]].append(arr[i * 2 + 1])
    graph[arr[i * 2 + 1]].append(arr[i * 2])

bfs(1)