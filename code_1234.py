# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# 8/18

def password(n):
    # 같은 문자가 연속한다면 삭제
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            n = n.replace(n[i:i + 2], '')
            # 연속 문자를 삭제한 새로운 문자열 n을 함수에 적용
            return password(n)

    # 연속하는 문자가 없다면 수정된 문자열 반환
    else:
        return n

for test_case in range(1, 11):
    num, pw = input().split()
    print(f'#{test_case} {password(pw)}')
