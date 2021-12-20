hour, minute = input().split()

hour = int(hour)
minute = int(minute)

minute -= 45
if minute < 0:
    hour -= 1
    if hour < 0:
        hour = 24 + hour
    minute = 60 + minute

print(str(hour) + " " + str(minute))