def solution(brown, yellow):
    rec = brown + yellow
    x = rec
    y = 1
    while x > y:
        y += 1
        x = rec // y
        if x * y != rec:
            continue
        if (y - 2) * (x - 2) == yellow:
            break
    answer = [x, y]
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))