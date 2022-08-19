# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
# 8/9


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    num = input()
    nums = []

    # 여백없이 주어진 숫자를 하나씩 리스트에 담기
    for n in num:
        nums.append(int(n))

    # 숫자의 개수 담을 리스트 생성
    counts = [0] * 10

    for i in nums:
        counts[i] += 1

    max_count = 0
    for j in range(len(counts)):
        if counts[j] >= max_count:  # 등호를 쓴 이유 : 카드 장수가 같을 때는 숫자가 큰 쪽을 출력하기 위해
            max_count = counts[j]
            max_num = j

    print(f'#{test_case} {max_num} {max_count}')
