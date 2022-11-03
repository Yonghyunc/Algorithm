# 백준 14501 : 퇴사


def talk(i, gain=0):
    global max_gain
    visited[i] = True
    if i + plans[i] < n:
        talk(i + plans[i], gain + gains[i])
        visited[i] = False
        talk(i + 1, gain)
    else:
        if gain > max_gain:
            max_gain = gain

# 수정을 좀 해줍시다

n = int(input())
plans = []
gains = []
for _ in range(n):
    t, p = map(int, input().split())
    plans.append(t)
    gains.append(p)
visited = [False] * n
print(plans)
print(gains)
max_gain = 0
talk(0)
print(max_gain)


