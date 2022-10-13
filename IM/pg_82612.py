# 프로그래머스 82612. 부족한 금액 계산하기

def solution(price, money, count):
    cost = 0
    for i in range(1, count + 1):
        cost += price * i
    print(cost)
    answer = cost - money
    if answer < 0:
        answer = 0
    return answer

print(solution(3, 20, 4))