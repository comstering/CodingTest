def remove_node(tree, node):
    while tree[node]:
        remove_node(tree, tree[node].pop())


def count_leaf(tree, node):
    count = 0
    if tree[node]:
        for i in tree[node]:
            count += count_leaf(tree, i)
    else:
        count = 1
    return count


def solution(tree, node, root_node):
    if node == root_node:
        return 0
    for i in range(len(tree)):
        if node in tree[i]:
            tree[i].remove(node)
            break
    remove_node(tree, node)
    return count_leaf(tree, root_node)


n = int(input())
tree = [[] for _ in range(n)]

node = list(map(int, input().split()))

root_node = 0

for i in range(n):
    if node[i] == -1:
        root_node = i
        continue

    tree[node[i]].append(i)

remove = int(input())

print(solution(tree, remove, root_node))