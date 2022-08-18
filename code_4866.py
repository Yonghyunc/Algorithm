# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
# 8/18
# 문제 잘못 이해함^^

# 괄호를 탐색하는 함수
def bracket(n, start, end):
    stack = []
    for i in range(len(n)):
        if n[i] == start:           # 여는 괄호를 스택에 넣음
            stack.append(n[i])

        elif n[i] == end:           # 닫는 괄호일 시 스택에서 top 제거
            if not stack:           # 스택이 비어있다면 0을 반환 (닫는 괄호가 더 많음)
                return False
            stack.pop()
    if not stack:                   # for문을 다 돌고 stack이 비었다면 괄호의 짝이 맞음
        return True
    else:                           # 그렇지 않다면 여는 괄호가 더 많음
        return False



t = int(input())

for test_case in range(1, t + 1):

    n = input()

    if bracket(n, '(', ')') and bracket(n, '{', '}'):        # 두 괄호의 쌍이 모두 맞으면
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')






