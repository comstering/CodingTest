def hanoi(n, t):
    if len(t[0]) == 0:
        if len(t[1]) % 2 == 0:
            t[0].append(t[1].pop())
            print(2, 1)
        else:
            t[2].append(t[1].pop())
            print(2, 3)
    elif len(t[0]) % 2 == 0:
        if len(t[1]) == 0:
            t[1].append(t[0].pop())
            print(1, 2)
        elif len(t[1]) % 2 == 0:
            if t[0][-1] < t[1][-1]:
                t[1].append(t[0].pop())
                print(1, 2)
            else:
                t[0].append(t[1].pop())
                print(2, 1)
        else:
            if t[1][-1] < t[2][-1]:
                t[2].append(t[1].pop())
                print(2, 3)
            else:
                t[1].append(t[2].pop())
                print(3, 2)
    else:
        if len(t[2]) == 0:
            t[2].append(t[0].pop())
            print(1, 3)
        elif len(t[2]) % 2 == 0:
            if t[0][-1] < t[2][-1]:
                t[2].append(t[0].pop())
                print(1, 3)
            else:
                t[0].append(t[2].pop())
                print(3, 1)
        else:
            if t[1][-1] < t[2][-1]:
                t[2].append(t[1].pop())
                print(2, 3)
            else:
                t[1].append(t[2].pop())
                print(3, 2)


num = int(input())
print(2 ** num - 1)
tower = [list(reversed(range(num))), [], []]
while len(tower[2]) < num:
    hanoi(num, tower)