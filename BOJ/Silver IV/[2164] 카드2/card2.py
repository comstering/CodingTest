from collections import deque

n = int(input())
card = [i for i in range(n, 0, -1)]
card = deque(card)

while len(card) > 1:
    card.pop()
    card.appendleft(card.pop())

print(card[0])