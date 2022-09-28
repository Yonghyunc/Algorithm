# 프로그래머스 42576 : 완주하지 못한 선수


def solution(participant, completion):
    answer = ''
    k = 0
    while k < len(participant):
        if participant[k] in completion:
            completion.remove(participant[k])
        else:
            answer = participant[k]
            break
        k += 1
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
