# 7465. 창용 마을 무리의 개수

def dfs(x):
    belong[x] = True

    for y in range(1, n + 1):
        if y in know[x] and not belong[y]:
            dfs(y)


t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    # 인덱스와 사람 번호의 숫자를 맞춰서 사용
    know = [[0] for _ in range(n + 1)]
    belong = [False] * (n + 1)

    # 무리의 수
    clan = 0

    # 연결관계 리스트
    for _ in range(m):
        a, b = map(int, input().split())
        know[a].append(b)
        know[b].append(a)

    # 한 무리가 어디까지 연결되어 있는지 확인
    for i in range(1, n + 1):
        if not belong[i]:
            clan += 1
            dfs(i)

    print(f'#{test_case} {clan}')
