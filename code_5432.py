# 5432. 쇠막대기 자르기
# string 실습 extra
# 8/17

t = int(input())

for test_case in range(1, t + 1):
    brackets = input()

    # 레이저를 #로 변환
    brackets = brackets.replace('()', '#')

    # 여는 괄호 넣을 스택
    stack = []

    # 막대기의 시작점, 끝점을 담을 리스트
    start = []
    end = []

    for i in range(len(brackets)):
        # 여는 괄호가 나오면 해당 인덱스를 stack 리스트에 넣어둠
        if brackets[i] == '(':
            stack.append(i)

        # 닫는 괄호가 나오면 해당 인덱스를 end 리스트에 넣어주고,
        # stack 리스트에 넣어두었던 인덱스 중 가장 최근의 것을 start 리스트에 넣어줌
        elif brackets[i] == ')':
            end.append(i)
            start.append(stack.pop())

    # 각 막대기 길이 사이에 몇 개의 레이저가 포함되는지 구함
    cut = 0

    for i in range(len(start)):
        stick = brackets[start[i] : end[i] + 1]
        cut += stick.count('#') + 1  # 잘린 막대기의 길이는 레이저 개수보다 하나 많음

    print(f'#{test_case} {cut}')
