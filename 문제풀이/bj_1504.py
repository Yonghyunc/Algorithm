# 백준 1504. 특정한 최단 경로

import sys
input = sys.stdin.readline

n, e = map(int, input().split())        # 정점, 간선
graph = [[] for _ in range(e)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

