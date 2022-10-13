# 프로그래머스 17682. 다트 게임


def solution(dartResult):
    sdt = ['A', 'S', 'D', 'T']  # A는 그냥 인덱스 자리 맞춰주기 위해 넣음
    stack = []
    n = False

    for dart in dartResult:
        if dart in sdt:
            num = stack.pop()
            multi = sdt.index(dart)
            stack.append(num ** multi)
            n = False

        elif dart == '*':
            num = stack.pop()
            if stack:
                pre_num = stack.pop()
                stack.append(pre_num * 2)
            stack.append(num * 2)
            n = False

        elif dart == '#':
            num = stack.pop()
            stack.append(-num)
            n = False

        else:                       # 숫자일 때,
            if n:
                stack.pop()
                stack.append(10)
            else:
                stack.append(int(dart))
            n = True
    return sum(stack)

print(solution('1D2S3T*'))
