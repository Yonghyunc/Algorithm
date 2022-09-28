# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

'''
한번에 key 값을 찾는 것 OK
한쪽 구간 탐색으로 key 값을 찾는 것 OK
오른쪽, 왼쪽 구간을 번갈아 탐색하여 key 값을 찾는 것 OK

BUT,
같은 구간을 연속적으로 탐색하는 것 X
오 -> 오 // 왼 -> 왼
'''


def binary(arr, low, high, key):
    global right, left, cnt
    if low > high:                  # 찾을 구간 없으면 return
        return

    middle = (low + high) // 2      # 중심 원소 인덱스

    if key == arr[middle]:          # 조건을 만족하는 값을 찾았다!
        cnt += 1
        return middle
    elif key < arr[middle]:         # 중심 원소보다 찾으려는 값이 더 작을 때 -> 왼쪽 구간 탐색
        if left:                    # 바로 이전에 왼쪽 구간을 탐색했으면 조건 불만족
            return
        left = True                 # 왼쪽 구간 방문 표시
        right = False               # 오른쪽 방문 여부는 초기화해줌
        return binary(arr, low, middle - 1, key)
    else:                           # 중심 원소보다 찾으려는 값이 더 클 때 -> 오른쪽 구간 탐색
        if right:                   # 바로 이전에 오른쪽 구간을 탐색했으면 조건 불만족
            return
        right = True                # 오른쪽 구간 방문 표시
        left = False                # 왼쪽 방문 여부는 초기화해줌
        return binary(arr, middle + 1, high, key)


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        right = False
        left = False
        binary(a, 0, n - 1, i)
    print(f'#{tc} {cnt}')