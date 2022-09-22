# 백준 1931 : 회의실 배정

import sys
n = int(sys.stdin.readline())

# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 시작시간 기준 정렬
meeting = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)])

# 종료시간 기준 정렬
meeting.sort(key=lambda x: x[1])

# 가장 빠른 종료 시간에서 시작
end = meeting[0][1]
cnt = 1
for i in range(1, n):
    if meeting[i][0] >= end:        # 다음 회의의 시작시간이 현재 종료 시간보다 같거나 늦으면
        cnt += 1                    # 회의 가능
        end = meeting[i][1]
print(cnt)
