# 2025. N줄 덧셈 (D1)

'''
[ 아이디어 ]


1. 입력받은 숫자까지의 range 함수를 사용하여 더함
--> 굳이 리스트로 넣을 필요가 있을까?


2. 바로 for문


'''

# 1

# n = int(input())

# numbers = list(range(n + 1))

# sum_num = 0
# for i in numbers:
#     sum_num += i

# print(sum_num)


# 2 

n = int(input())

sum_num = 0

for i in range(n + 1):
    sum_num += i

print(sum_num)
