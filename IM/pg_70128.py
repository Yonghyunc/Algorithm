# 프로그래머스 70128 : 내적


def solution(a, b):
    n = len(a)
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    return result
