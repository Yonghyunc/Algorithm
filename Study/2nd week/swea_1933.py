# 1933. 간단한 N의 약수 (D1)

'''
입력으로 1개의 정수 N 이 주어진다.

정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
 

[제약사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
 
[입력]
입력으로 정수 N 이 주어진다.

[출력]
정수 N 의 모든 약수를 오름차순으로 출력한다.

[입력 예시]
10

[출력 예시]
1 2 5 10
'''


## 첫번째 코드

N = int(input())

index = 1

while index <= N:
    if N % index == 0:
        print(index, end=' ')
    index += 1


## 두번째 코드

N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=' ')
