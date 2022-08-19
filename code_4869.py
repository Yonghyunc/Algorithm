# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기



t = int(input())



for test_case in range(1, t + 1):
    n10 = int(input())

    paper = [0, 1, 3]
    n = n10 // 10

    if n > 2:
        for i in range(3, n + 1):
            if i % 2 == 1:
                paper.append(paper[i - 2] * 4 + 1)
            else:
                paper.append(paper[i - 2] * 3 + 2 * (i // 2 - 1))

    print(f'{test_case} {paper[-1]}')
