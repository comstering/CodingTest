def solution(n):
    numstr = ''
    while(n>=3):
        numstr += str(n % 3)
        n //= 3
    numstr += str(n)

    answer = int(numstr, 3)

    return answer


print(solution(45))    # 7
print(solution(125))    # 229