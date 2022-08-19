# 7675. 통역사 성경이


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    # 문제에 제시된 부호 기준으로 문장 단위로 구분하여 리스트에 저장
    s = list(map(str, input().replace('.', '#').replace('!', '#').replace('?', '#').split('#')))

    # 마지막에 분리되는 공백 제거
    s.pop()

    print(f'#{test_case}', end=' ')

    # 문장별로 단어 분리하여 이름 여부 확인
    for i in range(n):
        word = list(map(str, s[i].split()))
        name = 0

        for j in range(len(word)):
            # 두 글자 이상으로 이루어진 단어
            if len(word[j]) > 1:
                if word[j][0].isupper() and word[j].isalpha() and word[j][1:].islower():
                    name += 1

            # 한 글자 이름 고려
            else:
                if word[j].isalpha() and word[j].isupper():
                    name += 1

        print(name, end=' ')
    print()