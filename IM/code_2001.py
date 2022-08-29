# 2001. 파리 퇴치


t = int(input())

for test_case in range(1, t + 1):

    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    fly_list = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            fly = []
            for k in range(j, j + m):
                fly.append(arr[k][i:i + m])
            fly_list.append(fly)

    sum_fly_list = []
    for i in range(len(fly_list)):
        sum_fly = 0
        for j in range(len(fly_list[i])):
            for k in range(len(fly_list[i][j])):
                sum_fly += fly_list[i][j][k]
        sum_fly_list.append(sum_fly)

    max_sum = 0
    for i in range(len(sum_fly_list)):
        if max_sum < sum_fly_list[i]:
            max_sum = sum_fly_list[i]

    print(f'#{test_case} {max_sum}')