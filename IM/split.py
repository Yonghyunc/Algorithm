a = input().split()             # ['ab', 'cd', 'ef']
b = list(input().split())       # ['ab', 'cd', 'ef']
c = list(input())               # ['a', 'b', ' ', 'c', 'd', ' ', 'e', 'f']
print(a)
print(b)
print(c)

q, w, e = input().split()       # 언패킹?
print(q, w, e)                  # ab cd ef

r, *t = input().split()
print(r, t)                     # ab ['cd', 'ef']
                                # ab ['cd'] 2개 받아도 뒤에껀 리스트로
print(type(r))                  # <class 'str'>
print(type(t))                  # <class 'list'>

g = "ab"
print(g.split())                  # ['ab']

# iterable 이 이미 리스트라면, iterable[:] 과 비슷하게 복사본을 만들어서 반환합니다.
# https://docs.python.org/ko/3/library/stdtypes.html#list
# ab cd ef