import calendar

def solution(a, b):
    day = calendar.weekday(2016, a, b)
    answer = "MON" if day == 0 else "TUE" if day == 1 else "WED" if day == 2 else "THU" if day == 3 else "FRI" if day == 4 else "SAT" if day == 5 else "SUN"
    return answer


print(solution(5, 24))