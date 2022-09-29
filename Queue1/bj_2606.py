# 백준 2606. 바이러스


def bfs(v):
    visited = [False] * (n + 1)
    queue = [v]
    cnt = 0

    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            cnt += 1

            for i in graph[t]:
                if not visited[i]:
                    queue.append(i)
    return cnt


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1) - 1)
