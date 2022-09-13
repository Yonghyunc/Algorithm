# 프로그래머스 60058 : 괄호 변환

# 0. 매개변수가 균형잡힌 괄호 문자열인지 확인
# "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 라는 지문이 있어서 필수는 아님
# if p.count('(') != p.count(')'):


def lge(u):
    global answer
    stack = []
    for bracket in u:
        if bracket == '(':
            stack.append('(')
            answer += '('
        else:
            if stack:
                stack.pop()
                answer += ')'
            else:  # ) 괄호가 ( 괄호보다 먼저 나온 경우,
                break
    if len(answer) == len(u):
        return answer

    v = p[len(answer):]
    kka(v)


def kka(v):
    # stack = []
    if v[0] != '(':
        v = '(' + v
    lge(v)

p = "()))((()"
answer = ""
lge(p)
print(answer)