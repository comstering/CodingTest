def solution(n):
    wm = "수박"
    wm *= n//2 + n % 2
    answer = wm[:n]
    return answer


print(solution(4))