class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.head = None

    def inorder_walk(self, node, arr=[]):
        if node == None: return

        self.inorder_walk(node.left, arr)
        arr.append(node.data)
        self.inorder_walk(node.right, arr)

        return arr

    def insert(self, data):
        node = Node(data)

        prev = None
        curr = self.head

        while curr != None:
            prev = curr

            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = prev

        if prev == None:  # empty tree, first node
            self.head = node
        elif data < prev.data:
            prev.left = node
        else:
            prev.right = node


def test():
    # Insert
    tree = Tree()
    for num in (12, 5, 2, 9, 18, 15, 13, 17,
                19):  # Introduction To Algorithms, page 295
        tree.insert(num)
    arr = tree.inorder_walk(tree.head)
    print('passed') if arr == [2, 5, 9, 12, 13, 15, 17, 18, 19
                               ] else print('failed')


if __name__ == '__main__':
    test()
