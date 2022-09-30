# 백준 1647. 도시 분할 계획


import sys
input = sys.stdin.readline


def find_set(k):
    if parents[k] != k:
        parents[k] = find_set(parents[k])
    return parents[k]


n, m = map(int, input().split())            # 집, 길
house = []
for _ in range(m):
    a, b, c = map(int, input().split())
    house.append((c, a, b))                 # 간선 비용, 연결 노드 순으로 삽입
house.sort()                                # 비용이 적은 순으로 오름차순 정렬
parents = list(range(n + 1))                # 대표자
road = 0
count = 0

for i in range(m):
    xr, yr = find_set(house[i][1]), find_set(house[i][2])

    if xr != yr:                    # 서로소일 때
        parents[yr] = xr            # 연결
        road += house[i][0]         # 유지 비용을 계속 더해줌
        count += 1                  # 연결된 간선 개수

    if count >= n - 2:              # 모든 집이 이어지려면 간선 개수가 n - 1 이어야 함,
        print(road)                 # 그렇다면 하나만 끊어지려면 간선 개수가 n - 2 이면 됨
        break