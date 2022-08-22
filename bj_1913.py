# 백준 1913 : 달팽이

n = int(input())
m = int(input())

# 하, 우, 상, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

snail = [[0] * n for _ in range(n)]
num = n * n
snail[0][0] = n * n
x = 0
y = 0

idx = 0
idy = 0

while num != 1:
    for d in range(4):
        x = x + dx[d]
        y = y + dy[d]

        while 0 <= x < n and 0 <= y < n:
            if snail[x][y] == 0:
                num -= 1
                snail[x][y] = num
                if num == m:
                    idx = x
                    idy = y
                x = x + dx[d]
                y = y + dy[d]
            else:
                break

        x = x - dx[d]
        y = y - dy[d]

for i in range(n):
    print(*snail[i])
print(idx + 1, idy + 1)

'''
idx = -1
idy = -1
반복문 바깥에서 정의를 해준 arr[0][0]의 숫자를 m으로 입력받을 경우,
idx 번호가 다르게 출력되는 오류가 있었다.

해당 코드를
idx = 0
idy = 0
으로 수정
'''
