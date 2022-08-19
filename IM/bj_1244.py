# 백준 1244. 스위치 켜고 끄기

# 걸린 시간 : 1시간 + 에러 찾기

'''
[반례]
3
0 0 0
1
2 2

# for문 범위 설정
if num > (sn / 2):
    ran = sn - num
에서 오류가 있었음

if num > (sn / 2):
    ran = sn - num + 1
으로 수정하니 성공

'''
# 코드를 작성하는 것은 어렵지 않았으나, 반례를 찾아 오류를 해결하는 과정이 어려웠다

sn = int(input())
switch = list(map(int, input().split()))

student = int(input())

for _ in range(student):
    sex, num = map(int, input().split())

    # 남학생인 경우,
    if sex == 1:
        # 배수의 개수만큼 반복
        for i in range(1, (sn // num) + 1):
            # 배수에 해당하는 스위치만 상태 변경
            switch[num * i - 1] = abs(switch[num * i - 1] - 1)

    # 여학생인 경우,
    else:
        # num 번 스위치의 인덱스는 num - 1
        n = num - 1

        # 받은 번호의 스위치 상태 변경
        switch[n] = abs(switch[n] - 1)

        # for문 범위 설정
        if num > (sn / 2):
            ran = sn - num + 1
        else:
            ran = num

        for i in range(1, ran):
            # 좌우 스위치가 값이 같으면, 상태 변경
            if switch[n - i] == switch[n + i]:
                switch[n - i], switch[n + i] = abs(switch[n - i] - 1), abs(
                    switch[n + i] - 1
                )

            # 같지 않으면 for문 종료
            else:
                break


for i in range(len(switch) // 20 + 1):
    print(*switch[i * 20 : i * 20 + 20])
