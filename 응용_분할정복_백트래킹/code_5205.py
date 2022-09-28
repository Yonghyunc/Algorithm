# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

def partition(arr, left, right):
    pivot = arr[left]           # 가장 왼쪽 값을 피벗으로
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:           # 피벗 값보다 더 큰 값이 나올 때까지 이동
            i += 1
        while i <= j and arr[j] >= pivot:           # 피벗 값보다 더 작은 값이 나올 때까지 이동
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]         # s가 e보다 크다면 자리 바꿔주기
    arr[left], arr[j] = arr[j], arr[left]           # 피벗값 자리 찾아주기
    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


for tc in range(1, int(input()) + 1):
    n = int(input())
    number = list(map(int, input().split()))
    quick_sort(number, 0, n - 1)
    print(f'#{tc} {number[n//2]}')
