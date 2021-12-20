a = int(input())
count = 0
while count < a:
    student = list(map(int, input().split()))
    num = student.pop(0)
    ave = sum(student) / num
    over = 0
    for i in student:
        if i > ave:
            over += 1
    count += 1
    print("{per:0.3f}%".format(per=over/num*100))