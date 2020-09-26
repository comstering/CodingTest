def solution(location):
    x = int(ord(location[0]) - ord('a')) + 1
    y = int(location[1])
    change = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
    count = 0
    for i in change:
        chx = x + i[0]
        chy = y + i[1]
        if chx > 0 and chy > 0:
            count += 1
    return count


lo = input()
print(solution(lo))