# 바이러스

n = int(input())

m = int(input())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
total = 0

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            global total
            total += 1
            dfs(next_v)

dfs(1)
print(total)