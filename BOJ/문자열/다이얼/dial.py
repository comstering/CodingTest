time = 0
for i in input():
    if "ABC".find(i) != -1:
        time += 3
    elif "DEF".find(i) != -1:
        time += 4
    elif "GHI".find(i) != -1:
        time += 5
    elif "JKL".find(i) != -1:
        time += 6
    elif "MNO".find(i) != -1:
        time += 7
    elif "PQRS".find(i) != -1:
        time += 8
    elif "TUV".find(i) != -1:
        time += 9
    elif "WXYZ".find(i) != -1:
        time += 10
print(time)