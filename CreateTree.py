#!/usr/bin/python3
import sys
from BinarySearchTree import BST


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


x = len(sys.argv)

if x < 8:
    print("Please give all nodes a Value")

else:
    root = BinaryTree(sys.argv[1])
    root.left = BinaryTree(sys.argv[2])
    root.left.left = BinaryTree(sys.argv[3])
    root.left.right = BinaryTree(sys.argv[4])
    root.right = BinaryTree(sys.argv[5])
    root.right.left = BinaryTree(sys.argv[6])
    root.right.right = BinaryTree(sys.argv[7])

    result = BST(root)
    if result:
        print("--Binary Search Tree--")
        print("Yes")
    else:
        print("--Binary Search Tree--")
        print("No")
