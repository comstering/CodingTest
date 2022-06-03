import sys
sys.setrecursionlimit(10 ** 6)

gears = []

for _ in range(4):
    gears.append(list(map(int, list(input()))))


def gear_turn(before_idx, idx, direction):
    if before_idx >= idx:
        if 0 < idx:
            if gears[idx - 1][2] != gears[idx][6]:
                gear_turn(before_idx, idx - 1, -direction)
    if before_idx <= idx:
        if idx < 3:
            if gears[idx + 1][6] != gears[idx][2]:
                gear_turn(before_idx, idx + 1, -direction)
    if direction == 1:
        gears[idx] = gears[idx][-1:] + gears[idx][:-1]
    elif direction == -1:
        gears[idx] = gears[idx][1:] + gears[idx][:1]


k = int(input())

abut_index = [(-1, 2), (6, 2), (6, 2), (6, -1)]

for _ in range(k):
    index, turn = map(int, input().split())
    gear_turn(index - 1, index - 1, turn)

answer = 0

count = 0
for gear in gears:
    if gear[0] == 1:
        answer += 2 ** count
    count += 1

print(answer)
