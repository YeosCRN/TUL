#!/usr/bin/python3

def BST(root):
    def numberlist(node):
        if node is None:
            return []
        left_node = numberlist(node.left)
        root_node = [node.data]
        right_node = numberlist(node.right)
        return left_node + root_node + right_node

    numbers = numberlist(root)
    for x in range(1, len(numbers)):
        if numbers[x] <= numbers[x - 1]:
            return False
    return True
