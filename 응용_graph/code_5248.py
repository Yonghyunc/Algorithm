# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기


def find(n):
    if pair[n]:                             # 신청서가 있으면
        for i in range(len(pair[n])):       # 신청된 조 전부
            if pair[n][i] not in done:      # 확인한 적 없으면
                done.append(pair[n][i])     # 확인 표시
                find(pair[n][i])            # 해당 번호의 신청서를 찾으러 이동
    return


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    pair = [[] for _ in range(n + 1)]
    for i in range(m):                                      # 신청서 각각의 번호 인덱스에 적어줌
        pair[number[i * 2]].append(number[i * 2 + 1])
        pair[number[i * 2 + 1]].append(number[i * 2])

    done = []           # 번호 확인용
    cnt = 0
    for i in range(1, n + 1):
        if not pair[i]:         # 신청되지 않은 번호는 -> 단독으로 조 구성
            done.append(i)
            cnt += 1
        else:                   # 신청된 번호는 -> 같은 조가 될 번호 전부 찾기
            if i not in done:
                cnt += 1
                find(i)
    print(f'#{tc} {cnt}')

