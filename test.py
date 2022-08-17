n = int(input())
arr = []
for i in range(n):
    arr.append(input().replace(' ', ''))


# arr90 = list((map(''.join, zip(*arr[-1 : -(n + 1) : -1]))))

# arr180 = list((map(''.join, zip(*arr90[-1 : -(n + 1) : -1]))))

# arr270 = list((map(''.join, zip(*arr180[-1 : -(n + 1) : -1]))))


def rotation(arr):
    return list((map(''.join, zip(*arr[-1 : -(n + 1) : -1]))))


print(rotation(arr))
