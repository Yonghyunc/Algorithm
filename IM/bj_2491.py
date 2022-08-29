# 백준 2491 : 수열

n = int(input())
nums = list(map(int, input().split()))

# 연속 길이를 넣을 리스트
con = [1]

# 오름차순
asc = 1
for i in range(n - 1):
    if nums[i] <= nums[i + 1]:
        asc += 1
    else:
        con.append(asc)
        asc = 1
else:
    con.append(asc)

# 내림차순
des = 1
for i in range(n - 1):
    if nums[i] >= nums[i + 1]:
        des += 1
    else:
        con.append(des)
        des = 1
else:
    con.append(des)

# 가장 긴 연속값 출력
print(max(con))

'''
두번의 실패의 반례
1
1
=> n이 1일 때는 반복문을 돌지 않음
==> con 리스트 안에 미리 최소값인 1을 넣어 놓음
---
2
1 1
=> if 문을 만족하는 값으로 끝나면 con 리스트 안에 append 되지 않음
==> for-else 문으로 해결
'''