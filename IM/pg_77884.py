# 프로그래머스 77884. 약수의 개수와 덧셈

# 뭔가 패턴이 있을텐데 그게 뭘까...


def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        num = number
        if num % 2 == 0:                    # 짝수일때,
            rest = 2
            # print(num, end=' : ')
            while num % 2 == 0:
                if num == 2 or num == 4:
                    rest -= 1
                    break
                num /= 2
                rest += 2
            # print(rest)
            if rest % 2 == 0:
                answer += number
            else:
                answer -= number

        else:                               # 홀수일때,
            rest = 2
            div = 3
            half = num // 2
            # print(num, end=' : ')
            while div < half and num > half:
                if num % div == 0:
                    rest += 2
                    num /= div
                    if num / div == 1:
                        rest -= 1
                        break
                div += 2
            # print(rest)
            if rest % 2 == 0:
                answer += number
            else:
                answer -= number

    return answer


print(solution(24, 27))