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

    def _search(self, node, data):
        if node == None or node.data == data:
            return node
        elif data > node.data:
            return self._search(node.right, data)
        else:
            return self._search(node.left, data)

    def search(self, data):
        node = self._search(self.head, data)

        return node != None

    def _search_iterative(self, node, data):
        while node != None and node.data == data:
            if data > node.data:
                node = node.right
            else:
                node = node.left

        return node

    def search_iterative(self, data):
        node = self._search(self.head, data)

        return node != None

    def _maximum(self, node):
        while node.right != None:
            node = node.right

        return node

    def maximum(self):
        if self.head == None:
            return None

        node = self._maximum(self.head)

        return node.data if node != None else None

    def _minimum(self, node):
        while node.left != None:
            node = node.left

        return node

    def minimum(self):
        if self.head == None:
            return None

        node = self._minimum(self.head)

        return node.data if node != None else None

    def _successor(self, node):
        if node.right != None:
            return self._minimum(node.right)

        parent = node.parent
        while parent != None and node != parent.left:
            node = parent
            parent = node.parent

        return parent

    def successor(self, data):
        node = self._search(self.head, data)
        if node == None:
            return None

        successor_node = self._successor(node)

        return successor_node.data if successor_node != None else None


def test():
    # Insert
    tree = Tree()
    for num in (12, 5, 2, 9, 18, 15, 13, 17,
                19):  # Introduction To Algorithms, page 295
        tree.insert(num)
    print('passed') if tree.inorder_walk(
        tree.head) == [2, 5, 9, 12, 13, 15, 17, 18, 19] else print('failed')

    # Search
    print('passed') if tree.search(17) == True else print('failed')
    print('passed') if tree.search(0) == False else print('failed')

    print('passed') if tree.search_iterative(17) == True else print('failed')
    print('passed') if tree.search_iterative(0) == False else print('failed')

    # Min/max
    print('passed') if tree.maximum() == 19 else print('failed')
    print('passed') if tree.minimum() == 2 else print('failed')

    # Successor
    print('passed') if tree.successor(5) == 9 else print('failed')
    print('passed') if tree.successor(17) == 18 else print('failed')

    tree = Tree()
    for num in (20, 6, 8, 15, 10, 9, 11):
        tree.insert(num)
    print('passed') if tree.successor(15) == 20 else print('failed')


if __name__ == '__main__':
    test()
