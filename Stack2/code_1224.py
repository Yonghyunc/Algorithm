# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
# 8/23

for test_case in range(1, 11):
    t = int(input())
    middle = input()
    stack = []
    back = ''

    for token in middle:
        # 연산자
        if token in '()+*':
            if not stack or token == '(':
                stack.append(token)

            elif token == '*':
                stack.append(token)

            elif token == '+':
                while stack and stack[-1] != '(':
                    back += stack.pop()
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    back += stack.pop()
                stack.pop()

        # 피연산자
        else:
            back += token

    # 스택에 남은게 있을 때
    while stack:
        back += stack.pop()

    # 연산
    for char in back:
        if char not in '+*':
            stack.append(int(char))

        else:
            x = stack.pop()
            y = stack.pop()

            if char == '+':
                stack.append(x + y)

            elif char == '*':
                stack.append(x * y)

    print(f'#{test_case} {stack[-1]}')




