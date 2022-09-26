# 전위 순회
def pre(k):
    print(k, end=' ')
    if k <= n and ch1[k]:
        pre(ch1[k])
        if ch2[k]:
            pre(ch2[k])


# 중위 순회
def inorder(k):
    if k <= n and ch1[k]:
        inorder(ch1[k])
    print(k, end=' ')
    if k <= n and ch2[k]:
        inorder(ch2[k])


# 후위 순회
def post(k):
    if k <= n and ch1[k]:
        post(ch1[k])
        if ch2[k]:
            post(ch2[k])
    print(k, end=' ')


n = 12  # 간선의 수
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

ch1 = [0] * (n + 1)
ch2 = [0] * (n + 1)

for i in range(n):
    if not ch1[arr[2 * i]]:
        ch1[arr[2 * i]] = arr[2 * i + 1]
    else:
        ch2[arr[2 * i]] = arr[2 * i + 1]

pre(1)
print()
inorder(1)
print()
post(1)
