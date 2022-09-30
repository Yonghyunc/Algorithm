# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    fire = []
    for i, c in enumerate(cheese[:n], start=1):     # 가장 처음 화덕에 n개의 피자를 넣은 상태
        fire.append((c, i))                         # 피자 번호를 함께 저장해줌

    idx = n
    while len(fire) > 1:                            # 화덕에 피자가 하나 남으면 끝남
        now, org = fire.pop(0)                      # 1번에서 피자를 꺼내 확인
        if now // 2 == 0 and idx < m:               # 치즈가 다 녹았고, 넣을 피자가 있으면
            fire.append((cheese[idx], idx + 1))     # 다음 피자를 넣음
            idx += 1
        elif now // 2 != 0:                         # 치즈가 덜 녹았으면
            fire.append((now // 2, org))            # 녹지 않은 치즈의 양을 화덕 마지막에 다시 넣음
    print(f'#{tc} {fire[0][1]}')                    # 마지막에 화덕에 남은 피자의 번호 출력