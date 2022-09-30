# 2819. 격자판의 숫자 이어 붙이기

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 가능한 한 모든 배열을 구하는 함수
def move(x, y, num):
    num += arr[x][y]                    # 해당 위치의 수를 배열에 넣어줌

    if len(num) == 7:                   # 7자리의 수를 만들었을 때,
        if num not in num_list:         # 해당 수가 중복되지 않으면
            num_list.append(num)        # 추가해줌
        return

    for d in range(4):                                      # 동서남북 방향으로 델타이동 해줌
        if 0 <= x + dx[d] < 4 and 0 <= y + dy[d] < 4:       # 범위에서 벗어나지 않으면 이동
            move(x + dx[d], y + dy[d], num)                 # 이동한 위치에서 델타이동


for tc in range(1, int(input()) + 1):

    # 입력을 받을 때 문자형으로 받되, 띄어쓰기는 제거함
    arr = [input().replace(' ', '') for _ in range(4)]
    num_list = []           # 모든 숫자 배열을 담을 리스트

    # 임의의 위치에서 시작하기 때문에, 모든 위치에서 시작하는 경우를 전부 고려
    for i in range(4):
        for j in range(4):
            move(i, j, "")
    print(f'#{tc} {len(num_list)}')