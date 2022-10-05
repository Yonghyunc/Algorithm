# 백준 2164 : 카드 2

# 큐로 풀면 시간 초과됨


from collections import deque

n = int(input())
card = deque(range(1, n + 1))

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(*card)