# 백준 14889. 스타트와 링크

import sys
input = sys.stdin.readline

def comb(team_a, k=0):
    global min_diff

    if len(team_a) == tn:
        print('a', team_a)
        team_b = []
        for i in range(n):
            if i not in team_a:
                team_b.append(i)
        print('b', team_b)

        sy_a = 0
        sy_b = 0
        for i in range(tn - 1):
            sy_a += arr[team_a[i]][team_a[i + 1]] + arr[team_a[i + 1]][team_a[i]]
            sy_b += arr[team_b[i]][team_b[i + 1]] + arr[team_b[i + 1]][team_b[i]]

        sy_a += arr[team_a[0]][team_a[-1]] + arr[team_a[-1]][team_a[0]]
        sy_b += arr[team_b[0]][team_b[-1]] + arr[team_b[-1]][team_b[0]]

        diff = abs(sy_a - sy_b)
        # print(diff)
        if min_diff > diff:
            min_diff = diff
        return

    if k == n:
        return

    team_a.append(k)
    comb(team_a, k + 1)
    team_a.remove(k)
    comb(team_a, k + 1)


n = int(input())
tn = n // 2
arr = [list(map(int, input().split())) for _ in range(n)]

min_diff = 100000
comb([])
print(min_diff)
