# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
# 성공

t = int(input())

for test_case in range(1, t + 1):
    n10 = int(input())

    # 십의 자리 앞 숫자를 인덱스 번호로 사용
    n = n10 // 10

    # 십의 자리 숫자와 인덱스 번호를 맞춰주기 위해 맨 앞에 0 추가
    paper = [0, 1, 3]

    if n > 2:
        for i in range(3, n + 1):
            paper.append(paper[i - 2] * 2 + paper[i - 1])

    print(f'#{test_case} {paper[n]}')

# 반복문을 반복할 때마다 paper 리스트가 원래 형태로 돌아간 뒤,
# 다시 for문 + append 메서드로 값을 넣어준다는 단점이 존재한다.
