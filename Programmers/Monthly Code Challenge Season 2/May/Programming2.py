def solution(numbers):
    answer = []
    for i in numbers:
        binI = bin(i)
        count = 0
        idx = -1
        while binI[idx] == '1':
            count += 1
            idx -= 1
        if count <= 1:
            answer.append(i + 1)
        else:
            answer.append(i + 2 ** (count - 1))
    return answer


print(solution([2, 7]))    # [3, 11]