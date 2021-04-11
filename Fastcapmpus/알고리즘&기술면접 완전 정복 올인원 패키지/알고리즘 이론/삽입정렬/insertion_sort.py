import random

def insertion(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break


data_list = random.sample(range(100), 50)
print(data_list)
insertion(data_list)
print(data_list)