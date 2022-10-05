# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    for _ in range(m):
        queue.append(queue.pop(0))
    print(f'#{tc} {queue[0]}')