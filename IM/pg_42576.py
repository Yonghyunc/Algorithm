# 프로그래머스 42576 : 완주하지 못한 선수


# def solution(participant, completion):
#     answer = ''
#     k = 0
#     while k < len(participant):
#         if participant[k] in completion:
#             completion.remove(participant[k])
#         else:
#             answer = participant[k]
#             break
#         k += 1
#     return answer


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))
