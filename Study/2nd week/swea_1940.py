# 1940. 가랏! RC카!

'''

RC (Radio Control) 카의 이동거리를 계산하려고 한다.

입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.

0 : 현재 속도 유지.
1 : 가속
2 : 감속

위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.

가속도의 단위는, m/s2 이며, 모두 양의 정수로 주어진다.

입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.

RC 카의 초기 속도는 0 m/s 이다.

[예제]

아래 예제 입력에서 정답은 3 이 된다.

입력         시간     RC 카의 속도 RC     카의 이동거리
1 2          1 sec          2 m/s                    2 m
2 1          2 sec          1 m/s                    3 m


[제약사항]

1. N은 2이상 30이하의 정수이다. (2 ≤ N ≤ 30)

2. 가속도의 값은 1 m/s2 혹은 2 m/s2 이다.

3. 현재 속도보다 감속할 속도가 더 클 경우, 속도는 0 m/s 가 된다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T, 다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스 첫 줄에는 Command 의 수 N이 주어지고, 둘째 줄부터, 매 줄마다 각각의 Command가 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''




T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    vel_now = 0 # 현재 속도
    dis = 0 # 이동거리

    for sec in range(1, N + 1):
        # 1. input() 개수가 다름 -- 리스트로 받기
        command_list = list(map(int, input().split()))

        if command_list[0] == 1:  # 가속(1)
            vel_now += command_list[1]

        elif command_list[0] == 2: # 감속(2)
            if vel_now < command_list[1]: # 현재 속도보다 감속할 속도가 더 클 경우
                vel_now == 0 
            else:
                vel_now -= command_list[1]

        else: # 속도 유지(0)
            vel_now


        dis += vel_now


    print(f'#{test_case} {dis}')

        

