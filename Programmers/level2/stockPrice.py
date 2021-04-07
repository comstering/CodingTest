def solution(prices):
    answer = [i - 1 for i in range(len(prices), 0, -1)]
    length = len(prices)
    prices.reverse()
    for i in range(length):
        data = prices.pop()
        for j in range(len(prices)):
            if data > prices[-j - 1]:
                answer[i] = j + 1
                break
    return answer


print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]