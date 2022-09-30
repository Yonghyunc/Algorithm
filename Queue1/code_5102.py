# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

from collections import deque


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        k = queue.popleft()

        for i in graph[k]:                      # 인접 노드 번호를 큐에 삽입
            if not visited[i]:                  # 확인하지 않았다면
                visited[i] = True               # 확인 표시 후
                queue.append(i)                 # 큐에 삽입
                cnt[i] = cnt[k] + 1             # 간선 수 + 1

            if i == g:                          # 도착 노드를 찾았다면
                return cnt[i]                   # 최소 간선 수 출력

    return cnt[g]                               # 연결되어 있지 않다면, 0 출력


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())            # 노드, 간선
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):                          # 양방향 인접 리스트
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v + 1)                 # 방문 처리
    cnt = [0] * (v + 1)                         # 최소 간선 수
    s, g = map(int, input().split())            # 출발 노드, 도착 노드
    print(f'#{tc} {bfs(s)}')

