# 백준 10157 : 자리배정

c, r = map(int, input().split())
k = int(input())

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [[0] * c for _ in range(r)]


num = 1
x = r - 1
y = 0
arr[r - 1][0] = 1


idx = ''
idy = 0

while num != c * r:
    for i in range(4):
        x = x + dx[i]
        y = y + dy[i]

        while 0 <= x < r and 0 <= y < c:
            if arr[x][y] == 0:
                num += 1
                arr[x][y] = num
                if num == k:
                    idx = r - x
                    idy = y + 1
                x = x + dx[i]
                y = y + dy[i]
            else:
                break

        x = x - dx[i]
        y = y - dy[i]

if k == 1:
    print(1, 1)
else:
    print(idy, idx)



