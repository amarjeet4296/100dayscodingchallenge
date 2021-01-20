class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.leftSize = 0

# Inserting a new Node.
def insert(root, data):
    if root == None:
        return newNode(data)

    # Updating size of left subtree.
    if data <= root.data:
        root.left = insert(root.left, data)
        root.leftSize += 1
    else:
        root.right = insert(root.right, data)
    return root

# Function to get Rank of a Node x.
def getRank(root, x):

    # Step 1.
    if root.data == x:
        return root.leftSize

    # Step 2.
    if x < root.data:
        if root.left == None:
            return -1
        else:
            return getRank(root.left, x)

    # Step 3.
    else:
        if root.right == None:
            return -1
        else:
            rightSize = getRank(root.right, x)
            return root.leftSize + 1 + rightSize

# Driver code
if __name__ == '__main__':
    arr = [12, 1, 4, 14, 15, 9, 7, 13, 3]
    n = len(arr)
    x = 12

    root = None
    for i in range(n):
        root = insert(root, arr[i])

    print("Rank of", x, "in stream is:", getRank(root, x))
