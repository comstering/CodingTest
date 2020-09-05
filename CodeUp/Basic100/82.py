num = input()
for i in range(1, 16):
    print(num + "*" + str(hex(i)).upper()[2:] + "=" + str(hex(int('0x' + num, 16) * i)).upper()[2:])