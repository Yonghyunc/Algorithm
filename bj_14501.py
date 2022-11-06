# 백준 14501 : 퇴사

'''
반례

3
1 5
3 15
1 5

4
1 5
4 15
3 10
1 5

'''

def talk(i, gain=0):
    global max_gain
    if i + plans[i] < n:
        talk(i + plans[i], gain + gains[i])
        talk(i + 1, gain)

    elif i + plans[i] == n:
        if gain + gains[i] > max_gain:
            max_gain = gain + gains[i]
    else:
        if gain > max_gain:
            max_gain = gain


n = int(input())
plans = []
gains = []
for _ in range(n):
    t, p = map(int, input().split())
    plans.append(t)
    gains.append(p)
max_gain = 0
talk(0)
print(max_gain)


