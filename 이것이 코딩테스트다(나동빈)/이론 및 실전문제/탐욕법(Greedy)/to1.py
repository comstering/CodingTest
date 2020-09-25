def solution(n, k):
    count = 0
    while True:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1

        if n == 1:
            break
    return count


print(solution(25, 5))
print()