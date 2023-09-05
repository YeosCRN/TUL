# TUL Internship Exercises

## Binary Search Tree

In this exercise, the code iterates through the nodes of a Binary Tree to confirm whether it is a Binary Search Tree or not. I personally chose this project because I have previously made the code in C language and wanted to replicate it with python code.

- This code is quite simple and supports the creation of a simple Binary Tree and of 2 levels from the root.

## Example

    $ ./CreateTree.py 3 5 1 4 2 6 0

## Output

    --Binary Search Tree--
    No

## Example

    $ ./CreateTree.py 4 2 1 3 6 5 7

## Output

    --Binary Search Tree--
    Yes

### All nodes must have a Value:

## Example

    $ ./CreateTree.py 3 5 1 4 2 6

## Output

    Please give all nodes a Value

### The input for the tree should be as follows:

    root
	root.left - root.left.left - root.left.right
	root.right - root.right.left - root.right.right
