# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오


def powerset(i, k, t):
    if i == k:
        s = 0
        for j in range(10):
            if used[j]:
                s += arr[j]
        if s == t:
            for j in range(10):
                if used[j]:
                    print(arr[j], end=' ')
            print()
    else:
        used[i] = 0
        powerset(i + 1, k, t)
        used[i] = 1
        powerset(i + 1, k, t)


arr = list(range(1, 11))
used = [0] * 10
powerset(0, 10, 10)
