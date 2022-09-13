# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

for test_case in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    complexity = 0

    # 각 열을 확인 !!
    for i in range(n):
        line = []
        for j in range(n):
            if table[j][i] != 0:
                line.append(table[j][i])

        # S극 성질을 가진 자성체 떨어뜨림
        while line[0] == 2:
            line.pop(0)
        # N극 성질을 가진 자성체 떨어뜨림
        while line[-1] == 1:
            line.pop()
        
        # 교착상태 개수 세기
        for k in range(1, len(line)):
            if line[k] == 2 and line[k - 1] == 1:
                complexity += 1
    print(f'#{test_case} {complexity}')