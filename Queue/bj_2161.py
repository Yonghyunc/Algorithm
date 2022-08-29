# 백준 2161 : 카드1

num = list(range(1, int(input()) + 1))

while len(num) != 1:            # 카드가 한 장 남을 때까지 반복
    print(num.pop(0), end=' ')  # 제일 위에 있는 카드 버림 + 출력
    move = num.pop(0)           # 카드를 한장 버린 후, 젤 위에 온 카드를
    num.append(move)            # 맨 뒤로 보냄

print(*num)         # 마지막에 남게 되는 카드 출력
