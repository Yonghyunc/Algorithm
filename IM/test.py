
p = input()
answer = ""

# 1) 입력이 빈 문자열인 경우, 빈 문자열 반환
if p == "":
    answer = ""


# 올바른 괄호 문자열
def correct(st):
    u = ""  # 앞 문자열 (균형 잡힌)
    stack = []
    for bracket in p:
        if bracket == "(":
            stack.append("(")
            u += "("
        else:
            if not stack:
                v = p[len(u):]
                break
            stack.pop()
            u += ")"


# 올바르지 않은 괄호 문자열
def incorrect(st):
    u = ""  # 앞 문자열 (균형 잡힌)
    stack = []
    for bracket in p:
        if bracket == ")":
            stack.append(")")
            u += ")"
        else:
            if not stack:
                v = p[len(u):]
                break
            stack.pop()
            u += "("


# 2) u, v로 분리
# 2-1) '('로 시작일 때, == u가 무조건 올바른 괄호 문자열
if p[0] == "(":
    correct(p)

# 2-1) ')'로 시작일 때, == u가 무조건 올바르지 않은 괄호 문자열
else:
    incorrect(p)

# 올바른 괄호 문자열일 경우에는 문자열에 붙여주고
# u가 올바르지 않을 경우에는
# '(' + v 재귀 결과 + ')' + 첫번째, 마지막 문자를 제거한 u를 뒤집은 문자열

# 올바르지 않은 괄호 문자열 처리하는 함수 (위는 일단 무시)
# 입력 매개변수가 올바르지 않다고 가정하고 만들기 (나중에 조건 주던지)
def in_cor(u):
    # v 재귀하는 함수....
    '(' + 'v 재귀 결과' + ')' +


