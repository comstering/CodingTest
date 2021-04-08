# 리스트로 힙을 사용
# 부모 Node 인덱스 = 자식 Node 인덱스 // 2
# 왼쪽 자식 Node 인데스 = 부모 Node 인덱스 * 2
# 오른쪽 자식 Node 인덱스 = 부모 Node 인덱스 * 2 + 1

# max heap 구현
class Heap:
    def __init__(self, data):
        self.heap_array = [None, data]
    def move_up(self, inserted_idx):
        if inserted_idx == 1:
            return False
        else:
            parent_idx = inserted_idx // 2
            if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
                return True
            else:
                return False
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array = [None, data]
        else:
            self.heap_array.append(data)
            inserted_idx = len(self.heap_array) - 1
            while self.move_up(inserted_idx):
                parent_idx = inserted_idx // 2
                self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
                inserted_idx = parent_idx
        return True
    def move_down(self, popped_idx):
        left_idx = popped_idx * 2
        right_idx = popped_idx * 2 + 1
        # case1: 왼쪽 자식 Node가 없을 때
        if left_idx >= len(self.heap_array):
            return False
        # case2: 오른쪽 자식 Node만 없을 때
        elif right_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_idx]:
                return True
            else:
                return False
        # case3: 오른쪽, 왼쪽 자식 Node가 다 있을 때
        else:
            if self.heap_array[popped_idx] < self.heap_array[left_idx] or self.heap_array[popped_idx] < self.heap_array[right_idx]:
                return True
            else:
                return False
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array.pop()
        popped_idx = 1
        while self.move_down(popped_idx):
            left_idx = popped_idx * 2
            right_idx = popped_idx * 2 + 1
            # case2: 오른쪽 자식 Node만 없을 때
            if right_idx >= len(self.heap_array):
                self.heap_array[popped_idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[popped_idx]
                popped_idx = left_idx
            # case3: 오른쪽, 왼쪽 자식 Node가 다 있을 때
            else:
                change_idx = left_idx if self.heap_array[left_idx] > self.heap_array[right_idx] else right_idx
                self.heap_array[popped_idx], self.heap_array[change_idx] = self.heap_array[change_idx], self.heap_array[popped_idx]
                popped_idx = change_idx
        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)