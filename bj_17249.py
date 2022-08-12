# 백준 17249. 태보태보 총난타
# 8/12
# https://www.acmicpc.net/problem/17249

shadow = input()


left_right = shadow.split('(^0^)')
# left, right = shadow.split('(^0^)')
# print(left.count('@'), left_right('@'))

left = left_right[0].count('@')
right = left_right[1].count('@')

print(left, right)


# ----------

for i in range(2):
    count = left_right[i].count('@')
    print(count, end=' ')
