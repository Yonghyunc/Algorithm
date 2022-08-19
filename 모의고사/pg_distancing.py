# 프로그래머스 : 거리두기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

def solution(places):
    result_list = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(5):
        wr = places[i]      # 테스트 케이스
        result = 1          # 반환값
        breaker = False     # 종료조건
        visited = [[False] * 5 for _ in range(5)]  # 방문여부

        if breaker:
            break
        for x in range(5):
            if breaker:
                break
            for y in range(5):
                if wr[x][y] == 'P':         # 사람이 있으면
                    visited[x][y] = True    # 기준점 방문 체크 하고

                    if breaker:
                        break
                    for v in range(4):      # 상하좌우 확인
                        x2 = x + dx[v]
                        y2 = y + dy[v]

                        if 0 <= x2 < 5 and 0 <= y2 < 5:   # 인덱스 범위 내의

                            # 체크하지 않은 사람 자리
                            if wr[x2][y2] == 'P' and not visited[x2][y2]:
                                result = 0  # 실패
                                breaker = True

                            # 빈좌석일 때
                            elif wr[x2][y2] == 'O':
                                if breaker:
                                    break
                                for w in range(4):                      # 다시 상하좌우 확인
                                    x3 = x2 + dx[w]
                                    y3 = y2 + dy[w]

                                    if 0 <= x3 < 5 and 0 <= y3 < 5:
                                        if wr[x3][y3] == 'P' and not visited[x3][y3]:   # 체크하지 않은 사람 자리 있으면
                                            result = 0  # 실패
                                            breaker = True
                            # 칸막이
                            else:
                                pass

        result_list.append(result)

    return result_list

a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(a))