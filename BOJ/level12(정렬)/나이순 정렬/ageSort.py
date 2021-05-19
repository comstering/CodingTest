n = int(input())
userList = []
for i in range(n):
    user = input().split()
    userList.append((int(user[0]), user[1]))
for i in sorted(userList, key=lambda x: (x[0])):
    print(i[0], i[1])
