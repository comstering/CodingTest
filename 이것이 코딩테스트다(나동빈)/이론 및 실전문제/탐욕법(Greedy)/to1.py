def solution(n, k):
    count = n % k
    n -= (n % k)
    while n >= k:
        n //= k
        count += 1
    return count


print(solution(25, 5))
print(solution(17, 4))