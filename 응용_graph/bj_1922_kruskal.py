# 백준 1922. 네트워크 연결

'''
모든 컴퓨터가 연결이 되어 있어야 한다.
모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라.

=> MST, kruskal
'''


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])       # 경로 압축
    return parent[node]


n = int(input())        # 컴퓨터의 수
m = int(input())        # 연결의 수
computer = []
for _ in range(m):
    a, b, c = map(int, input().split())
    computer.append([c, a, b])              # 가중치 먼저

computer.sort()                             # 비용 기준 오름차순 정렬!!!!
parent = list(range(n + 1))
cost = 0                                    # 총 비용
cnt = 1                                     # 종료 조건

for i in range(m):
    x, y = computer[i][1], computer[i][2]
    root_x, root_y = find_set(x), find_set(y)
    if root_x != root_y:
        cnt += 1
        cost += computer[i][0]
        parent[root_y] = root_x
    if cnt == n:
        break
print(cost)

