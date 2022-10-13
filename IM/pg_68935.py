# 프로그래머스 68935. 3진법 뒤집기

def solution(n):
    three = []              # 앞뒤 반전된 3진법
    while n > 0:
        three.append(n % 3)
        n = n // 3

    num = three.pop(0)
    while three:
        rem = three.pop(0)
        num = num * 3 + rem

    return num

solution(45)