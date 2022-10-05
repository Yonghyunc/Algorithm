# 백준 1759. 암호 만들기

alp = 'abcdefghijklmnopqrstuvwxyz'
consonant = 'aeiou'


def per(n, m, k, now):
    global pos

    if n == k:
        if cnt.count(1) >= 1 and cnt.count(2) >= 2:
            print(*pos, sep='')
        return
    for i in range(k, m - n + 1 + k):
        if not visited[i] and i >= now:
            pos.append(order[i][1])
            cnt.append(order[i][2])
            visited[i] = True
            per(n, m, k + 1, i)
            pos.remove(order[i][1])
            cnt.remove(order[i][2])
            visited[i] = False


l, c = map(int, input().split())
code = input().split()
order = [0] * c
for i in range(c):
    if code[i] in consonant:    # 1은 자음
        order[i] = [alp.index(code[i]), code[i], 1]
    else:                       # 2은 모음
        order[i] = [alp.index(code[i]), code[i], 2]
order.sort()
# print(order)
pos = []
cnt = []
visited = [False] * c
per(l, c, 0, 0)

