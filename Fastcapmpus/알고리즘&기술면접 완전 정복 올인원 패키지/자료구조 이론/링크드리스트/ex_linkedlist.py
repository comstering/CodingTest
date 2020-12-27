class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def deleteNode(self, data):
        if self.head is None:
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                print("data: ", data)
                print("next: ", node.next.data)
                return
            node = node.next
        print("해당 데이터가 없습니다.")

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

def nodePrint():
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print(node.data)

def insertNode(beforeData, newNode):
    node = head
    search = True
    while search:
        if node.data == beforeData:
            search = False
        else:
            node = node.next
    node_next = node.next
    node.next = newNode
    newNode.next = node_next


class doubleNode:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class doubleNodeMgmt:
    def __init__(self, data):
        self.head = doubleNode(data)
        self.tail = self.head

    def add(self, data):
        if self.head is None:
            self.head = doubleNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = doubleNode(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = doubleNode(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node is None:
                    return False
            newNode = doubleNode(data)
            before_new = node.prev
            before_new.next = newNode
            newNode.prev = before_new
            newNode.next = node
            node.prev = newNode
            return True

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head is None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head is None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False


if __name__ == "__main__":
    # Linked List 1
    print("Linked List 1")
    node1 = Node(1)
    head = node1
    for index in range(2, 10):
        add(index)
    nodePrint()
    print()

    # Linked List 2
    print("Linked List 2")
    node3 = Node(1.5)
    insertNode(1, node3)
    nodePrint()

    linkedList1 = NodeMgmt(0)
    linkedList1.desc()
    for data in range(1, 10):
        linkedList1.add(data)
    linkedList1.desc()
    print()

    # Linked List 3
    print("Linked List 3")
    linkedList1 = NodeMgmt(0)
    linkedList1.desc()
    print(linkedList1.head)
    linkedList1.deleteNode(0)
    print(linkedList1.head)

    linkedList1 = NodeMgmt(0)
    linkedList1.desc()
    for data in range(1, 10):
        linkedList1.add(data)
    linkedList1.desc()
    linkedList1.deleteNode(4)
    linkedList1.desc()
    linkedList1.deleteNode(9)
    linkedList1.desc()
    linkedList1.search(6)
    print()

    # Linked List 4
    print("Linked List 4")
    double_linked_list = doubleNodeMgmt(0)
    for data in range(1, 10):
        double_linked_list.add(data)
    double_linked_list.desc()
    node3 = double_linked_list.search_from_head(3)
    print(node3.data)
    node3 = double_linked_list.search_from_head(10)
    if node3:
        print(node3.data)
    else:
        print("No data")
    node3 = double_linked_list.search_from_tail(3)
    print(node3.data)
    node3 = double_linked_list.search_from_tail(10)
    if node3:
        print(node3.data)
    else:
        print("No data")
    double_linked_list.insert_before(1.5, 2)
    double_linked_list.desc()