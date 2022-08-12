# 백준 2941. 크로아티아 알파벳
# 8/12
# https://www.acmicpc.net/problem/2941


# 다른 코드

c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
c_count = 0

for c in c_alpha:
    if c in word:
        # 크로아티아 알파벳을 문자 #로 변환
        word = word.replace(c, '#')

print(len(word))
