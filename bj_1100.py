# 백준 1100 : 하얀 칸

chess = [input() for _ in range(8)]

piece = 0

# 짝수 행
for i in range(0, 8, 2):        # 0, 2, 4, 6
    for j in range(0, 8, 2):
        if chess[i][j] == 'F':
            piece += 1

# 홀수 행
for i in range(1, 8, 2):        # 1, 3, 5, 7
    for j in range(1, 8, 2):
        if chess[i][j] == 'F':
            piece += 1

print(piece)
