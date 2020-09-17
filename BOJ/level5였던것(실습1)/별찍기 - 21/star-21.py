num = int(input())
count = 0
length = 0

while count < num * 2:
    if count % 2 == 0:
        while length < num:
            if length % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
            length += 1
    else:
        while length < num:
            if length % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
            length += 1
    print()
    length = 0
    count += 1