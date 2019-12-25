class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_value(self.root, Node(new_val))

    def search(self, find_val):
        return self.search_value(self.root, find_val)

    def insert_value(self, parent, new_node):
        if new_node.value > parent.value:
            if parent.right is None:
                parent.right = new_node
            else:
                self.insert_value(parent.right, new_node)
        elif new_node.value < parent.value:
            if parent.left is None:
                parent.left = new_node
            else:
                self.insert_value(parent.left, new_node)

    def search_value(self, parent, find_val):
        if parent.value == find_val:
            return True
        elif parent.value > find_val:
            if parent.left is None:
                return False
            else:
                self.search_value(parent.left, find_val)
        elif parent.value < find_val:
            if parent.right is None:
                return False
            else:
                self.search_value(parent.right, find_val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))