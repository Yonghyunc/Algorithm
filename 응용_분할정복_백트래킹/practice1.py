# 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오

'''
[input]
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0
'''


def partition(l, r):
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(l, r):
    if l < r:
        s = partition(l, r)
        quick_sort(l, s - 1)
        quick_sort(s + 1, r)


arr = list(map(int, input().split()))
n = len(arr)
quick_sort(0, n - 1)
print(*arr)
