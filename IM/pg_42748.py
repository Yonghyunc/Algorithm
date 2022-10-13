# 프로그래머스 42748. K번째 수


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new = array[i - 1:j]
        new.sort()
        answer.append(new[k - 1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
