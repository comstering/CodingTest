note = input().split()

note = list(map(int, note))


note1 = [1, 2, 3, 4, 5, 6, 7, 8]
note2 = [8, 7, 6, 5, 4, 3, 2, 1]

if note == note1:
    print("ascending")
elif note == note2:
    print("descending")
else:
    print("mixed")
