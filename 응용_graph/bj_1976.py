# 백준 1976. 여행 가자

# 여행 계획에 속한 도시들이 집합이면 됨


def find_set(node):
    if node != parent[node]:
       parent[node] = find_set(parent[node])
    return parent[node]


n = int(input())
m = int(input())
parent = list(range(n + 1))
city = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(i, n):
        if arr[j] == 1:
            city.append([i + 1, j + 1])
# print(city)

plan = list(map(int, input().split()))
result = 'NO'
for i in range(m - 1):
    x, y = plan[i], plan[i + 1]
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root


print(parent)