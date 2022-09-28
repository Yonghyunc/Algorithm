def dfs(i, n, c):
    if c == 3:
        return
    else:
        visited[i] = 1
        friends[i] = 1
        for j in range(n + 1):
            if adjM[i][j] == 1 and visited[j] == 0:
                dfs(j, n, c + 1)
        visited[i] = 0


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    adjM = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1

    visited = [0] * (n + 1)
    friends = [0] * (n + 1)
    dfs(1, n, 0)
    print(f'#{tc} {sum(friends) - 1}')