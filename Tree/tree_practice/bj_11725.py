# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

# def find(i):
#


n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n - 1)]
# print(arr)
# find(0)

ch1 = [[] for _ in range(n + 1)]
ch2 = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ch1[a].append(b)
    ch2[b].append(a)
print(ch1)
print(ch2)