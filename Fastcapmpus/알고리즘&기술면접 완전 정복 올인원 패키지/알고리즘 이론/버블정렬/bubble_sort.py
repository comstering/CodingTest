import random

def bubble(data):
    for i in range(len(data) - 1):
        no_swap = True
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                no_swap = False
        if no_swap:
            print("break: ", i)
            break


data_list = random.sample(range(100), 50)
print(data_list)
bubble(data_list)
print(data_list)