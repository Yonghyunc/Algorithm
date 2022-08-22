# 1223. [S/W 문제해결 기본] 6일차 - 계산기2
# 8/22


for test_case in range(1, 11):
    t = int(input())  # 테스트 케이스 길이
    middle = input()  # 중위표기법
    back = ''  # 후위표기법
    stack = []

    for token in middle:
        # token 이 연산자라면
        if token in '*+':

            # 곱셈 연산자 (무조건 우선)
            if token == '*':
                stack.append(token)

            # 덧셈 연산자 (무조건 나중)
            elif token == '+':
                while stack and stack[-1] != '+':
                    back += stack.pop()
                stack.append(token)

        # token 이 피연산자라면
        else:
            back += token

    # 스택에 남은 값이 있다면
    while stack:
        back += stack.pop()

    # ---
    for char in back:
        # char 이 피연산자라면
        if char not in '*+':
            stack.append(int(char))

        # 연산자라면
        else:
            y = stack.pop()  # 연산자 뒤
            x = stack.pop()  # 연산자 앞
            if char == '+':
                stack.append(x + y)
            elif char == '*':
                stack.append(x * y)

    print(f'#{test_case} {stack[-1]}')
