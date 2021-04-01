def solution(nums):
    length = len(nums) // 2
    phonekets = len(set(nums))
    answer = length if length <= phonekets else phonekets
    return answer


print(solution([3, 1, 2, 3]))    # 2
print(solution([3, 3, 3, 2, 2, 4]))    # 3
print(solution([3, 3, 3, 2, 2, 2]))    # 2