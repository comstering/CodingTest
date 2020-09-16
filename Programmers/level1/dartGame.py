def solution(dartResult):
    score = []
    num = ''
    for i in dartResult:
        if i.isdecimal():
            num += i
        elif i == 'S':
            score.append(int(num) ** 1)
            num = ''
        elif i == 'D':
            score.append(int(num) ** 2)
            num = ''
        elif i == 'T':
            score.append(int(num) ** 3)
            num = ''
        elif i == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif i == '#':
            score[-1] *= -1
    answer = sum(score)
    return answer


print(solution('1S2D*3T'))    # 37
print(solution('1D2S#10S'))    # 9
print(solution('1D2S0T'))    # 3
print(solution('1S*2T*3S'))    # 23
print(solution('1D#2S*3S'))    # 5
print(solution('1T2D3D#'))    # -4
print(solution('1D2S3T*'))    # 59