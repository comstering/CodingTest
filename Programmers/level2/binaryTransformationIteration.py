def solution(s):
    count = 0
    zeroCount = 0
    while s != '1':
        count += 1
        zeroCount += s.count('0')
        middleS = s.replace('0', '')
        s = bin(len(middleS))[2:]
    answer = [count, zeroCount]
    return answer


print(solution('110010101001'))    # [3, 8]
print(solution('01110'))    # [3, 3]
print(solution('1111111'))    # [4, 1]