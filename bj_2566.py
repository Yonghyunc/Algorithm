# 백준 2566 : 최댓값

arr = [list(map(int, input().split())) for _ in range(9)]

# 첫 번째 값으로 설정해둠
max_value = arr[0][0]
max_i = 0
max_j = 0

for i in range(9):          # 행 순회
    for j in range(9):      # 열 순회
        if arr[max_i][max_j] < arr[i][j]:   # 더 큰 값으로 교체
            max_value = arr[i][j]
            max_i = i
            max_j = j

print(max_value)
print(max_i + 1, max_j + 1)


