# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
# 성공


# for문 외부에 paper 리스트 할당
paper = [0] * 31
paper[0:3] = [0, 1, 3]

# paper 리스트를 채우는 함수, 한번 채우면 그 값은 다시 계산 X
def ten(n):
    if paper[n] == 0:       # 계산된 적 없는 인덱스에 대해서만 계산
        paper[n] = paper[n - 2] * 2 + paper[n - 1]


t = int(input())

for test_case in range(1, t + 1):
    n10 = int(input())

    # 십의 자리 숫자를 리스트 인덱스로 사용
    n = n10 // 10

    # 십의 자리 숫자 (+ 1) 에 맞춰서 함수 적용 반복 -- 함수에 조건이 있어서 계산이 반복되지는 않음
    if n > 2:
        for i in range(3, n + 1):
            ten(i)

    print(f'#{test_case} {paper[n]}')
