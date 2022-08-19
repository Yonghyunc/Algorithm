# 연습문제 : 부분집합 합
# 8/10 일차 문제
# 8/11 해결

# 입력 형태가 -7, -3, -2, 5, 8 처럼 콤마로 구분되어 있다고 가정

numbers = list(map(int, input().split(',')))  # 집합을 리스트 형태로 받음
n = len(numbers)


subset = [[0] for _ in range(1 << n)]

for i in range(1 << n):
    sub = []
    for j in range(n):
        if i & (1 << j):
            sub.append(numbers[j])
    subset[i] = sub

# 모든 부분집합의 합을 담을 리스트
all_sum = []

for i in range(len(subset)):
    sub_sum = 0  # 각각의 부분집합의 합
    for j in range(len(subset[i])):
        sub_sum += subset[i][j]
    all_sum.append(sub_sum)

all_sum.remove(0)  # 각 부분집합의 합의 초기값을 0으로 설정하여 공집합의 합은 무조건 0으로 나옴 -> 제거 필요

if 0 in all_sum:
    print(True)

else:
    print(False)
