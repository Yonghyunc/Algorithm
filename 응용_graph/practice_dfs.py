# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로 출력
# 시작 정점 = 1

'''
# input
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(n):
    visited[n] = True       # 방문 표시
    print(n, end=' ')       # 방문한 정점 번호 출력
    for i in graph[n]:      # 인접한 정점으로 이동
        if not visited[i]:  # 방문한 적 없을 경우에만
            dfs(i)


arr = list(map(int, input().split()))
n = len(arr) // 2
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)     # 방문 여부 확인

for i in range(n):              # 인접 리스트 생성
    graph[arr[i * 2]].append(arr[i * 2 + 1])
    graph[arr[i * 2 + 1]].append(arr[i * 2])

dfs(1)