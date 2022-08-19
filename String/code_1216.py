# 1216. [S/W 문제해결 기본] 3일차 - 회문2
# 8/16


for _ in range(10):

    t = int(input())

    str1 = [input() for _ in range(100)]    # 입력받은 문자열

    str2 = list(map(''.join, zip(*str1)))   # 문자열 가로 세로 바꿈

    max_pal = 0     # 회문의 최대 길이

    end = 0     # for문 종료 조건 (변수 선언)

    # 긴 회문부터 찾기

    # 중첩된 for문을 모두 빠져나오기 위해 for문마다 if문 사용
    if end: # 0은 False, 1은 True이기 때문에 종료조건을 if end: 로만 두어도 됨
        break
    for i in range(99, -1, -1):     # 99번째 인덱스부터 반대로

        if end:
            break
        for k in range(100):    # 100개의 행을 탐색
            if end:
                break

            for j in range(100 - i + 1):    # 100 - 회문의 길이만큼 반복

                if str1[k][j: j + i] == str1[k][j + i - 1:j - 1:-1]:    # 회문인지 판별
                    max_pal = i     # 회문이라면 해당 인덱스를 max_pal에 할당
                    end = 1     # 종료 조건 실행

                if str2[k][j: j + i] == str2[k][j + i - 1:j - 1:-1]:
                    max_pal = i
                    end = 1

    print(f'#{t} {max_pal}')
