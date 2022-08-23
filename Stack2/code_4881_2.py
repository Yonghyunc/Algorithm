

def number(choice, x):
    global min_sum      # 최소값
    global cho_sum      # 고른 숫자의 합

    if cho_sum > min_sum:       # 합이 최소값을 넘어가면 가지치기
        return

    if len(choice) == n:        # n개의 숫자를 고르면
        if min_sum > cho_sum:   # 최소값과 숫자의 합 비교
            min_sum = cho_sum
        return

    for y in range(n):                  # 열에 대한 반복문
        if not visited[y]:
            visited[y] = True
            choice.append(arr[x][y])
            cho_sum += arr[x][y]

            # 재귀함수
            number(choice, x + 1)       # 행 번호는 하나씩 늘림

            # 원상복귀
            visited[y] = False
            choice.pop()
            cho_sum -= arr[x][y]


for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n   # 숫자의 선택 여부 확인
    choice = []             # 뽑은 숫자를 담을 리스트
    min_sum = 1000000       # 최소값
    cho_sum = 0             # 뽑은 숫자의 합
    number([], 0)           # 함수 실행

    print(f'#{test_case} {min_sum}')