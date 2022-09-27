# 1865. 동철이의 일 분배

def probability(k, work):
    global max_work

    if k == n:                      # 모든 직원에게 일을 할당했다면
        work *= 100                 # 성공 확률을 구함
        if work > max_work:
            max_work = work
        return

    for i in range(n):                          # k 직원이 수행할 수 있는 일
        if ef[k][i] != 0 and not worked[i]:     # 능률이 0이 아니고, 다른 직원이 수행하지 않은 일
            work *= ef[k][i] / 100              # 능률을 구하고 있던 성공 확률에 곱해줌
            if work >= (max_work / 100):        # 곱해준 값이 max_work 보다 작으면 앞으로 모든 능률이 1이 나와도 더 커지지 않음
                worked[i] = True                # i번 일을 수행함
                if k < n:                       # 아직 일을 안 한 사람이 있을 때
                    probability(k + 1, work)    # 그 사람이 할 일을 구하러 감
            work /= ef[k][i] / 100              # 원상복구
            worked[i] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    ef = []
    for _ in range(n):
        ef.append(list(map(int, input().split())))
    max_work = 0
    worked = [False] * n
    probability(0, 1)
    print(f'#{tc}', '%.6f'%max_work)
