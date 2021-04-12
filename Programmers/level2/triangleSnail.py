def solution(n):
    data = n * (n + 1) // 2
    answer = [0 for i in range(data)]
    data_list = [i for i in range(data, 0, -1)]
    length = n
    index = 0
    cycle = 0
    while length > 0:
        if (n - length) % 3 == 0:
            for i in range(length):
                index += i + (cycle * 2)
                answer[index] = data_list.pop()
        elif (n - length) % 3 == 1:
            for i in range(length):
                index += 1
                answer[index] = data_list.pop()
        elif (n - length) % 3 == 2:
            for i in range(length):
                index -= (n - i - cycle)
                answer[index] = data_list.pop()
            cycle += 1
        length -= 1
    return answer


print(solution(4))    # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(solution(5))    # [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
print(solution(6))    # [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]