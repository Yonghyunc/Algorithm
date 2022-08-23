# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
# 8/23

for test_case in range(1, int(input()) + 1):
    # 두 자리 이상의 숫자가 나올 수 있으므로 공백기준 분리해서 리스트에 저장
    back = list(map(str, input().split()))
    stack = []

    for token in back:
        # 피연산자
        if token not in '+-*/.':
            stack.append(token)

        # .이 나오면 연산 종료
        elif token == '.':
            # stack에 값이 하나이면
            if len(stack) == 1:
                print(f'#{test_case} {stack[-1]}')
                break
            # stack에 남은 값이 여러개이면
            else:
                print(f'#{test_case} error')
                break

        # 연산자
        else:
            # 연산을 할 만큼 숫자가 있으면
            if len(stack) >= 2:
                # stack에서 연산할 숫자를 뽑아냄
                y = int(stack.pop())
                x = int(stack.pop())

                # 연산 결과를 다시 stack에 저장
                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                elif token == '/':
                    stack.append(x // y)            # /는 결과가 실수로 나와서 fail.....

            # 연산을 할 만큼 숫자가 없으면
            else:
                # stack.append('error')
                print(f'#{test_case} error')
                break


