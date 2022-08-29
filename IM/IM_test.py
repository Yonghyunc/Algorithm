# 총 테스트 케이스 개수
t = int(input())

for test_case in range(1, t + 1):
    # 신입 사원의 수, 최소 인원, 최대 인원
    n, low, high = map(int, input().split())

    # 신입 사원들의 어학점수
    scores = list(map(int, input().split()))

    # 1. 어학점수 오름차순 정렬
    scores = sorted(scores)
    # print(scores)

    # 2. 점수별 개수 카운트
    score_cnt = []
    cnt = 1
    for i in range(n - 1):
        if scores[i] == scores[i + 1]:
            cnt += 1
        else:
            score_cnt.append(cnt)
            cnt = 1
    else:
        score_cnt.append(cnt)   # 마지막 값

    # 3. 점수가 3개 뿐일 때,
    if len(score_cnt) == 3:
        for score in score_cnt:
            # 조건 불만족
            if score < low or score > high:
                result = -1
                break
        # 조건 만족
        else:
            result = max(score_cnt) - min(score_cnt)

    # 4. 3개 이상일 때,
    else:
        # 4-1. A, B, C반 분리
        cla = []    # 분리한 반을 넣을 리스트
        for i in range(1, len(score_cnt) - 1):
            # print(f'a: {score_cnt[:i]}, other: {score_cnt[i:]}')

            # 조건을 만족하는 A반 분리
            if low <= sum(score_cnt[:i]) <= high:
                a = score_cnt[:i]
                other = score_cnt[i:]

                # 나올 수 있는 모든 B반과 C반 케이스 (적어도 1개 이상)
                for j in range(1, len(other)):
                    # print(other[:j], other[j:])
                    cla.append([a, other[:j], other[j:]])

        # print(cla)

        # 4-2. 최소 학생 수와 최대 학생 수 조건을 만족하는 반의 조합 찾기
        all_list = []
        for i in range(len(cla)):
            sum_list = []
            for j in range(3):
                # 조건을 만족하면, 반별 합을 리스트에 넣음
                if low <= sum(cla[i][j]) <= high:
                    sum_list.append(sum(cla[i][j]))
                    pass
                else:
                    break
            # A, B, C반 모두 조건을 만족해야만 함
            if len(sum_list) == 3:
                all_list.append(sum_list)
        # print(all_list)

        # 4-3. 결과 구하기
        # 조건을 만족하는 조합이 없다면 -1 출력
        if len(all_list) == 0:
            result = -1
        # 조건을 만족하는 조합이 있다면,
        else:
            result = 100    # 기본값은 최대로 설정
            # 가장 작은 최대값과 최소값의 차를 구함
            for i in range(len(all_list)):
                if max(all_list[i]) - min(all_list[i]) < result:
                    result = max(all_list[i]) - min(all_list[i])
                    # print(result)

    print(f'#{test_case} {result}')