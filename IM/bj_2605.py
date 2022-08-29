# 백준 2605: 줄 세우기

n = int(input())
move = list(map(int, input().split()))
student = []

for i, v in enumerate(move):
    student.insert(i - v, i + 1)
print(*student)