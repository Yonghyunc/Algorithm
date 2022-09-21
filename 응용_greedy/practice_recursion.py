# 선택 정렬 함수를 재귀적 알고리즘으로 작성


def SelectionSort(i, n):
    if i == n - 1:
        return

    min_idx = i
    for j in range(i, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    SelectionSort(i + 1, n)


arr = [2, 4, 6, 1, 9, 8, 7, 0]
n = len(arr)
SelectionSort(0, n)
print(arr)