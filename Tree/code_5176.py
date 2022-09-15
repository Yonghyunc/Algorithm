# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

def inorder(k):
    global num
    if k <= n:
        inorder(2 * k)
        number[tree[k]] = num
        num += 1
        inorder(2 * k + 1)


# 완전 이진 트리
for tc in range(1, int(input()) + 1):
    n = int(input())

    tree = list(range(n + 1))

    number = [0] * (n + 1)
    num = 1
    inorder(1)

    print(f'#{tc} {number[1]} {number[n//2]}')