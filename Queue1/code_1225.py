# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
# 큐

def password():
    while num[-1] != 0:         # 0일 경우, 프로그램 종료
        for i in range(1, 6):   # 1사이클
            v = num.pop(0)
            v_plus = v - i
            if v_plus < 0:      # 0보다 작으면 0으로 유지되어야 함
                v_plus = 0
            num.append(v_plus)
            if num[-1] == 0:    # 0일 경우, for문 종료
                break


for _ in range(10):
    t = int(input())    # 테스트 케이스 번호
    num = list(map(int, input().split()))

    password()
    print(f'#{t}', *num)