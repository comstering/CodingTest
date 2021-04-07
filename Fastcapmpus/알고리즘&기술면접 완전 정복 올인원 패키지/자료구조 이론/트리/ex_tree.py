class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif self.current_node.value > value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched:
            # 삭제할 노드가 Leap Node일 경우(Child Node가 없을 경우) case1
            if self.current_node.left == self.current_node.right is None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None

            # 삭제할 노드에 Child Node가 1개 있을 경우 case2
            elif self.current_node.left is not None and self.current_node.right is None:
                if value < self.current_node.value:
                    self.parent.left = self.current_node.left
                else:
                    self.parent.right = self.current_node.left
            elif self.current_node.left is None and self.current_node.right is not None:
                if value < self.current_node.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right

            # 삭제할 노드에 Child Node가 2개 있을 경우(+Child Node에 또 Child Node가 있는 경우)
            elif self.current_node.left is not None and self.current_node.right is not None:    # case3
                if value < self.parent.value:    # case3-1
                    self.change_node = self.current_node.right
                    self.change_parent = self.current_node.right
                    while self.change_node.left:
                        self.change_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right:
                        self.change_parent.left = self.change_node.right
                    else:
                        self.change_parent.left = None
                    self.parent.left = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left
                else:    # case3-2
                    self.change_node = self.current_node.right
                    self.change_parent = self.current_node.right
                    while self.change_node.left:
                        self.change_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right:
                        self.change_parent.left = self.change_node.right
                    else:
                        self.change_parent.left = None
                    self.parent.right = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left

            del self.current_node
            return True
        else:
            return False


head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(4)
BST.insert(3)
BST.insert(0)
BST.insert(6)
BST.insert(-1)
BST.insert(8)
print(BST.search(3))
print(BST.search(7))
print(BST.search(-1))

# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서 이진탐색트리에 입력, 검색, 삭제
import random

# 0 ~ 999 숫자 중 100개 랜덤 선택
bst_nums = set()
while len(bst_nums) < 100:
    bst_nums.add(random.randint(0, 999))

# 선택된 100개의 숫자를 이진 탐색트리에 입력, 단, 임의로 루트 노드는 500으로 설정
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개 숫자 검색
for num in bst_nums:
    if not binary_tree.search(num):
        print("Search Failed", num)

# 입력한 100개 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) < 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자 삭제
for del_num in delete_nums:
    if not binary_tree.delete(del_num):
        print("Delete Failed", del_num)