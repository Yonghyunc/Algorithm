# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

def ride(k, cnt):
    global min_cnt

    if cnt > min_cnt:                   # 가지치기 조건 (이미 최소가 아니라면 확인 X)
        return

    if k + battery[k] >= n:             # 종점에 갈 수 있을 때
        if cnt < min_cnt:               # 최소 교환횟수 구함
            min_cnt = cnt
        return min_cnt

    cnt += 1
    for i in range(k + 1, k + battery[k] + 1):      # 현재 정류장의 다음 정류장부터 최대로 갈 수 있는 정류장까지
        if i < n:                                   # 정류장이 존재한다면 (인덱스가 있다면)
            ride(i, cnt)


for tc in range(1, int(input()) + 1):
    n, *battery = map(int, input().split())
    battery.insert(0, 0)                        # 정류장 번호와 인덱스 번호 맞춰주기 위함
    min_cnt = n
    ride(1, 0)
    print(f'#{tc} {min_cnt}')
