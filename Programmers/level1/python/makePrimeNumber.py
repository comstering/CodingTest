import math


def checkPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0
    for i in nums:
        for j in nums[nums.index(i) + 1:]:
            for k in nums[nums.index(j) + 1:]:
                num = i + j + k
                answer += checkPrime(num)

    return answer


print(solution([1, 2, 3, 4]))    # 1
print(solution([1, 2, 6, 7, 4])) # 4
