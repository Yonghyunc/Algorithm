# 프로그래머스 72410 : 신규 아이디 추천

pos = ['-', '_', '.']


def solution(new_id):
    # 1단계 : 대문자 -> 소문자
    new_id = new_id.lower()

    # 2단계 : 소문자, 숫자, -, _, . 를 제외한 모든 문자 제거
    erase = []
    for w in new_id:
        if w.islower() or w.isdigit() or w in pos:
            pass
        else:
            erase.append(w)

    for e in erase:
        new_id = new_id.replace(e, "")

    # 3단계 : 2번 이상 연속된 마침표 -> 하나의 마침표
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    # 4단계 : 처음과 끝에 위치한 마침표 제거
    new_id = new_id.lstrip(".").rstrip(".")

    # 5단계 : new_id가 빈문자열이라면, "a" 대입
    if new_id == "":
        new_id = "a"

    # 6단계 : new_id가 16자 이상이라면, 15자로 맞춰주기 (끝이 .이라면 제거)
    new_id = new_id[:15].rstrip(".")

    # 7단계 : new_id가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id


solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
