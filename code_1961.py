# 1961. 숫자 배열 회전
# string 실습 extra


# 배열 90도씩 돌리는 함수 선언
def rotation(arr):
    return list((map(''.join, zip(*arr[::-1]))))


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    print(f'#{test_case}')

    # N x N 행렬 입력 받기 (리스트 내 문자열)
    arr = [input().replace(' ', '') for i in range(n)]

    # 함수 적용하여 각 각도로 돌린 배열 할당
    arr90 = rotation(arr)
    arr180 = rotation(arr90)
    arr270 = rotation(arr180)

    # for문 통해 출력
    for i in range(n):
        print(arr90[i], arr180[i], arr270[i])
