# 백준 17281. ⚾

'''
[아이디어]

1번 선수는 4번 타자로 고정.
bfs


'''


n = int(input())        # 이닝 수
players = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * 9 for _ in range(n)]
print(players)
print(visited)

out = 0
k = 0
base = [0, 0, 0, 0]                 # 루상의 주자 (인덱스 맞춰주기 위해 4)
while n != 0:                       # 타석 반복
    for i in range(1, 10):          # 1번부터 9번 타자
        pass