def solution(lottos, win_nums):
    answer = []
    count = [0, 0]
    for i in lottos:
        if i in win_nums:
            count[0] += 1
            count[1] += 1
    zero = lottos.count(0)
    count[0] += zero
    for i in count:
        answer.append(7-i if 7 - i <= 6 else 6)
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))    # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))    # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))    # [1, 1]