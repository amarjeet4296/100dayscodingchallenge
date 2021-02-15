class Node:
    def __init__(self, key, left=None, right=None):

        self.key = key
        self.left = left
        self.right = right

def printVertical(node, dist, dict):

    if node is None:
        return
    dict.setdefault(dist, []).append(node.key)
    printVertical(node.left, dist - 1, dict)
    printVertical(node.right, dist + 1, dict)


def printVerticalTree(root):
    dict = {}
    printVertical(root, 0, dict)

    for value in dict.values():
        print(value)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)

    printVerticalTree(root)
