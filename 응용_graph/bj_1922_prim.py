# 백준 1922. 네트워크 연결

from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        # 인접 정점에 대해 가중치와 정점 정보를 힙에 삽입
        for next_node, w in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (w, next_node))

    return cost


n = int(input())        # 컴퓨터의 수
m = int(input())        # 연결의 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(1))