import queue

# FIFO Queue
print("FIFO QUEUE")
fifo_queue = queue.Queue()
fifo_queue.put("funcoding")
fifo_queue.put(1)
print("size:", fifo_queue.qsize())
print(fifo_queue.get())
print(fifo_queue.get())
print()

# LIFO Queue
lifo_queue = queue.LifoQueue()
lifo_queue.put("funcoding")
lifo_queue.put(1)
print("size:", lifo_queue.qsize())
print(lifo_queue.get())
print(lifo_queue.get())
print()

# Priority Queue
priority_queue = queue.PriorityQueue()
priority_queue.put((10, "korea"))
priority_queue.put((5, 1))
priority_queue.put((15, "china"))
print("size:", priority_queue.qsize())
print(priority_queue.get())
print(priority_queue.get())
print(priority_queue.get())

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현
queue_list = list()
def enqueue(data):
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)
print(queue_list)
print(len(queue_list))
print(dequeue())
print(dequeue())
print(queue_list)
print(len(queue_list))