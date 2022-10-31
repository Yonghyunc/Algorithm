# 백준 10158. 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


nt = t - (w - p)
if (nt // w) / 2 != 0:
    p = nt % w
else:
    p = w - (nt % w)

nt = t - (h - q)
if (nt // h) / 2 != 0:
    q = (nt % h)
else:
    q = h - (nt % h)

print(p, q)






