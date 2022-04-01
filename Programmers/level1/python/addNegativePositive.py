def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
    return answer


print(solution([4, 7, 12], [True, False, True]))    # 9
print(solution([1, 2, 3], [False, False, True]))    # 0