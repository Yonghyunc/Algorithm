# 백준 2789. 유학 금지
# 8/12
# https://www.acmicpc.net/problem/2789


no = "CAMBRIDGE"

email = input()

for i in no:
    email = email.replace(i, '')

print(email)
