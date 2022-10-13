# 프로그래머스 118666. 성격 유형 검사하기


def solution(survey, choices):
    alp = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = [0] * 8
    answer = ''

    for i in range(len(choices)):
        if choices[i] <= 3:
            score[alp.index((survey[i][0]))] += 4 - choices[i]
        elif choices[i] >= 5:
            score[alp.index((survey[i][1]))] += choices[i] - 4

    for i in range(4):
        if score[2 * i] >= score[2 * i + 1]:
            answer += alp[2 * i]
        else:
            answer += alp[2 * i + 1]
    return answer


survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
print(solution(survey, choices))