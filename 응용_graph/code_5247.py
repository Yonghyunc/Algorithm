# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

from collections import deque

cal =[
    lambda x: x * 2,
    lambda x: x + 1,
    lambda x: x - 10,
    lambda x: x - 1,
]


def bfs(v, cnt):
    queue = deque()
    queue.append([v, cnt])                  # 현재 값, 연산 횟수

    while queue:
        k, cnt = queue.popleft()
        for i in range(4):
            val = cal[i](k)                                 # 연산 값
            if 0 < val <= 1000000 and not visited[val]:     # 연산의 중간 결과가 범위 내에 있으며, 연산한 적 없을 때
                visited[val] = True                         # 연산 여부 표시
                queue.append([val, cnt + 1])                # 다음 연산을 위해 큐에 삽입
            if val == m:                                    # m을 찾으면
                return cnt + 1                              # 이전 연산 횟수 + 1 을 반환


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = [False] * 1000001                             # 연산 결과의 범위만큼의 리스트를 만들어줌
    ans = bfs(n, 0)
    print(f'#{tc} {ans}')






# def calculator(n, m, cnt):
#     print('n', n, 'cnt', cnt)
#     # print(already)
#     global min_cnt
#
#     if n == m:
#         if cnt < min_cnt:
#             min_cnt = cnt
#         return
#
#     if cnt > min_cnt:
#         return
#
#     cnt += 1
#
#     # visited = [False] * 4
#     for i in range(4):
#         # if i < 2:       # 숫자가 커지는 연산
#         if 0 < cal[i](n) <= m + 10:
#             if i < 2 and cal[i](n) > m * 2:
#                 continue
#             if i >= 2 and cal[i](n) < m - 10:
#                 continue
#             # if i == 1 and cal[i](n) < m // 2:
#             #     continue
#             # visited[i] = True
#             already.append(cal[i](n))
#             calculator(cal[i](n), m, cnt)
        # if i >= 2:
        #     if m < cal[i](n) and (cal[i](n) not in already) and not visited[i]:
        #         visited[i] = True
        #         already.append(cal[i](n))
        #         cnt += 1
        #         calculator(cal[i](n), m, cnt)