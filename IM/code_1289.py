# 1289. 원재의 메모리 복구하기

for test_case in range(1, int(input()) + 1):
    original = list(map(int, map(' '.join, input())))

    cnt = 0     # 수정 횟수
    idx = 51    # 메모리 길이를 초과한 인덱스 번호로 변수 선언
    memory = 0
    for i in range(len(original)):
        # 메모리 값이 1이고, 이전 값이 1이 아닐 때 (즉, 수정이 필요할 때)
        if original[i] == 1 and memory != 1:
            cnt += 1
            idx = i     # 해당 인덱스 이후부터는 값이 1임

        # 1로 변경된 이후 처음 나온 0값에 대해 다시 수정
        if i > idx and original[i] == 0 and memory != 0:
            cnt += 1

        memory = original[i]    # 현재 메모리 저장 (다음과 비교 위해)

    print(f'#{test_case} {cnt}')

