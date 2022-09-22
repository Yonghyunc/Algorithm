# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())    # n: 컨테이너 / m: 트럭

    # 내림차순으로 저장
    container = sorted(map(int, input().split()), reverse=True)
    truck = sorted(map(int, input().split()), reverse=True)

    weight = 0
    traveled = [False] * m      # 이미 운행을 한 트럭인지 아닌지 표시
    for i in range(n):
        for j in range(m):
            if container[i] <= truck[j] and not traveled[j]:    # 적재 가능하고, 운행하지 않은 트럭 있으면
                weight += container[i]                          # 화물 무게 추가
                traveled[j] = True                              # 트럭 운송 여부 체크
                break                                           # 해당 화물에 대한 반복 중단
    print(f'#{tc} {weight}')