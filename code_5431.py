# 5431. 민석이의 과제 체크하기


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    student = list(range(1, n + 1))
    submit = list(map(int, input().split()))

    for i in range(k):
        student.remove(submit[i])

    print(f'#{test_case}', *student)