# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임


def chk(p, idx):
    check = sorted(p)
    for j in range(len(check) - 2):

        # triplet 여부 확인 -> 만족하는 경우가 있을 시 바로 함수 종료
        if check[j] == check[j + 1] == check[j + 2]:
            score[idx] += 1
            return

    # run 여부 확인
    else:
        check2 = sorted(list(set(check)))       # 556677처럼 같은 수가 반복해서 나오면 정렬 후 run 검사 불가 -> 중복 제거 후 run 검사
        if len(check2) >= 3:                    # 중복 제거 후 남은 인자가 3개 이상일 때만 run 검사
            for k in range(len(check2) - 2):
                if check2[k] + 1 == check2[k + 1] and check2[k + 1] + 1 == check2[k + 2]:
                    score[idx] += 1
                    return


for tc in range(1, int(input()) + 1):
    card = list(map(int, input().split()))

    one = []
    two = []
    score = [0, 0]
    result = 0

    for i in range(0, 12, 2):
        one.append(card[i])         # player 1
        two.append(card[i + 1])     # player 2

        # triplet, run 확인
        if i >= 4:
            chk(one, 0)
            chk(two, 1)

        if score[0] >= score[1] and score[0] > 0:       # player 1이 승리하는 경우 -> 같은 순번에 둘 다 성공해도 player 1이 이기는 불공정 게임
            result = 1
            break
        elif score[1] > score[0]:                       # player 2가 승리하는 경우
            result = 2
            break

    print(f'#{tc} {result}')

