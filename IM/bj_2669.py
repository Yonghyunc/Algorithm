# 백준 2669 : 직사각형 네개의 합집합의 면적 구하기

rectangle = [list(map(int, input().split())) for _ in range(4)]
coordinate = []

for i in range(4):
    # 오른쪽 아래 좌표 번호만 저장
    for x in range(rectangle[i][0], rectangle[i][2]):
        for y in range(rectangle[i][1], rectangle[i][3]):
            # 이미 저장된 좌표면 저장 X
            if [x, y] not in coordinate:
                coordinate.append([x, y])

print(len(coordinate))