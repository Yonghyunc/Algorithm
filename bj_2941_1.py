# 백준 2941. 크로아티아 알파벳
# 8/12
# https://www.acmicpc.net/problem/2941


c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
c_count = 0

for c in c_alpha:
    if c in word:
        # 크로아티아 알파벳의 개수를 구함
        c_count += word.count(c)
        # 중복으로 계산되지 않도록 크로아티아 알파벳을 문자 #로 변환
        word = word.replace(c, '#')

# 나머지 알파벳의 개수를 구함
w_count = len(word) - word.count('#')

# 크로아티아 알파벳 개수 + 일반 알파벳 개수
print(c_count + w_count)
