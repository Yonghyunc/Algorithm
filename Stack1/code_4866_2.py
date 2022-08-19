# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
# 8/18


t = int(input())

for test_case in range(1, t + 1):

    n = input()

    stack = []

    yes = 0

    for i in range(len(n)):
        if len(n) > 0:
            if n[i] in ('(', '{'):      # 여는 괄호 나오면 스택에 저장
                stack.append(n[i])

            elif n[i] == ')':           # 닫는 소괄호 나오면
                if stack:
                    if stack[-1] == '(':    # 스택의 마지막 원소가 여는 소괄호일 때,
                        stack.pop()         # 스택 마지막 원소 삭제
                    else:
                        break
                else:
                    break

            elif n[i] == '}':           # 닫는 중괄호 나오면
                if stack:
                    if stack[-1] == '{':    # 스택의 마지막 원소가 여는 중괄호일 때,
                        stack.pop()         # 스택 마지막 원소 삭제
                    else:
                        break
                else:
                    break
        else:
            break


    else:
        if not stack:
            yes = 1

    print(f'#{test_case} {yes}')
