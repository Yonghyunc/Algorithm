# 4466. 최대 성적표 만들기

for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    score = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{tc} {sum(score[:k])}')
