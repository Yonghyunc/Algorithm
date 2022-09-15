# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙


'''
최소 힙
마지막 노드의 조상 노드 값들의 합
'''


# 힙 삽입 연산
def heap_push(num):
    heap.append(num)
    c = len(heap) - 1
    p = c // 2

    # 루트 노드이거나 최소힙 조건을 만족하지 못하면 종료
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


# 조상찾기 연산
def find_fore(n):
    global cnt
    cnt += heap[n]
    if n:
        find_fore(n // 2)

for tc in range(1, int(input()) + 1):

    n = int(input())
    nums = list(map(int, input().split()))

    heap = [0]

    for num in nums:
        heap_push(num)

    cnt = - heap[-1]

    find_fore(n)

    print(f'#{tc} {cnt}')
