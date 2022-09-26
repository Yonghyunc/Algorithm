# 프로그래머스 1845 : 폰켓몬

def solution(nums):
    n = len(nums)
    cnt = 0
    kind = set(nums)
    if len(kind) >= n//2:
        cnt = n//2
    else:
        cnt = len(kind)
    return cnt


nums = [3,3,3,2,2,4]
solution(nums)
