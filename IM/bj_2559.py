# 백준 2559 : 수열
# 시간제한 때문에 슬라이딩 윈도우로 풀어야 하는 문제!!


n, k = map(int, input().split())
nums = list(map(int, input().split()))

def temp(nums, k):
    max_sum = -100 * k
    start = 0
    curr_sum = 0

    for end, val in enumerate(nums):
        curr_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= nums[start]
            start += 1
    return max_sum

print(temp(nums, k))


'''
시간 초과 코드

temp_list = []
for i in range(0, n - k + 1):
    temp = 0
    for j in range(k):
        temp += nums[i + j]
    temp_list.append(temp)
print(max(temp_list))
'''

'''
시간 초과 코드

import sys
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_tem = -100 * k
def temp(s):
    global max_tem
    tem = 0
    for i in range(s, s + k):
        tem += nums[i]
    if max_tem < tem:
        max_tem = tem
    if s < n - k:
        temp(s + 1)

temp(0)
print(max_tem)
'''