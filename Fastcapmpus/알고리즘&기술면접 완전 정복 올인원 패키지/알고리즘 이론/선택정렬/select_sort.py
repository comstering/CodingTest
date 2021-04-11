import random

def select(data):
    for i in range(len(data) - 1):
        minidx= i
        for j in range(i + 1, len(data)):
            if data[minidx] > data[j]:
                minidx = j
        data[i], data[minidx] = data[minidx], data[i]


data_list = random.sample(range(100), 10)
print(data_list)
select(data_list)
print(data_list)