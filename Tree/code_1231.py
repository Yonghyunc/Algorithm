# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

# 중위 순회 함수
def inorder(n):
    if n:
        inorder(ch1[n])
        print(alp[n], end='')
        inorder(ch2[n])


for test_case in range(1, 11):
    n = int(input())

    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    alp = [0] * (n + 1)  # 알파벳을 담을 리스트
    for _ in range(n):
        case = list(input().split())
        alp[int(case[0])] = case[1]
        if len(case) >= 3:  # 자식노드가 하나 이상 있을 때,
            ch1[int(case[0])] = int(case[2])
        if len(case) == 4:  # 두 개의 자식노드가 있을 때,
            ch2[int(case[0])] = int(case[3])
    # print(alp)  # [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']
    # print(ch1)  # [0, 2, 4, 6, 8, 0, 0, 0, 0]
    # print(ch2)  # [0, 3, 5, 7, 0, 0, 0, 0, 0]

    print(f'#{test_case}', end=' ')
    inorder(1)
    print()
