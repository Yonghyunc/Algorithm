# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리


from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


for tc in range(1, int(input()) + 1):
    n, e = map(int, input().split())        # 정점 수, 간선 수
    graph = [[] for _ in range(n + 1)]
    INF = 999999999
    distance = [INF] * (n + 1)

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(0)
    print(f'#{tc} {distance[-1]}')




# --------------프림-------------------

# def prim(start):
#     visited = [False] * (n + 1)
#     heap = [(0, start)]
#     cost = 0
#
#     while heap:
#         min_dist, min_node = heappop(heap)
#         if visited[min_node]:
#             continue
#
#         visited[min_node] = True
#         cost += min_dist
#
#         if min_node == n:
#             break
#
#         for next_node, dist in graph[min_node]:
#             if not visited[next_node]:
#                 heappush(heap, (dist, next_node))
#
#     return cost
#
#
# for tc in range(1, int(input()) + 1):
#     n, e = map(int, input().split())        # 정점 수, 간선 수
#     graph = [[] for _ in range(n + 1)]
#     for _ in range(e):
#         a, b, c = map(int, input().split())
#         graph[a].append((b, c))
#         graph[b].append((a, c))
#
#     print(f'#{tc} {prim(0)}')