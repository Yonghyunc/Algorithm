# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
# 8/18

# 노드의 연결 여부를 파악하는 함수
def dfs(s, e):
    visited[s] = True

    for next in pair[s]:
        if not visited[next]:
            dfs(next, e)

    # 두 노드가 연결되어 있다면 (s 노드부터 길을 찾아가다가 g 노드가 나오면)
    if visited[e] == True:
        global yes
        yes = 1

for _ in range(10):
    # 테스트 케이스, 순서쌍 개수
    tc, n = map(int, input().split())

    yes = 0

    all_num = list(map(int, input().split()))

    # 각 숫자 노드에 연결된 노드를 저장 (0 ~ 2개)
    pair = [[] for _ in range(100)]

    # 짝수 인덱스는 리스트 번호, 홀수 인덱스는 짝수 인덱스 번호의 리스트에 저장
    for i in range(1, 2 * n):
        if i % 2 == 1:
            pair[all_num[i - 1]].append(all_num[i])

    visited = [False] * 100

    dfs(0, 99)

    print(f'#{tc} {yes}')

