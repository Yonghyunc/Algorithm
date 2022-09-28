# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬


def merge(left, right):
    merged_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[n//2]} {cnt}')