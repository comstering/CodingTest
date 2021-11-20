toSchool = int(input())
toPcRoom = int(input())
toAcademy = int(input())
toHome = int(input())

total = toSchool + toPcRoom + toAcademy + toHome

minute = total // 60
second = total % 60

print(minute)
print(second)