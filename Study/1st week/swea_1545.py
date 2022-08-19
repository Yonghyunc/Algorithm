# 1545. 거꾸로 출력해 보아요 (D1)

'''
주어진 숫자부터 0까지 순서대로 찍어보세요
아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

N N-1 N-2 ..... 0
'''


num = int(input())

num_list = list(range(num + 1))


for i in sorted(num_list, reverse=True):
    print(i, end = ' ')