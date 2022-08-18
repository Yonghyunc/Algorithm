# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
# 8/18

def seq(n):
    # 같은 문자가 연속한다면 삭제
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            n = n.replace(n[i:i + 2], '')
            # 연속 문자를 삭제한 새로운 문자열 n을 함수에 적용
            return seq(n)

    # 연속하는 문자가 없다면 문자열의 길이 반환
    else:
        return len(n)


t = int(input())

for test_case in range(1, t + 1):
    print(f'#{test_case} {seq(input())}')

