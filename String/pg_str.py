# 프로그래머스 : 숫자 문자열과 영단어
# 8/12
# https://school.programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    eng_num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for eng in eng_num:
        s = s.replace(eng, eng_num[eng])

    return int(s)
