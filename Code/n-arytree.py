
class NaryTreeNode(object):
    def __init__(self, data=None):
        """Initialize this n-ary tree node with the given data."""
        self.data = data
        self.children = []

    def __repr__(self):
        """Return a string representation of this n-ary tree node."""
        return 'NaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return len(self.child) == 0


class NaryTree(object):
    def __init__(self, key=None):
        self.size = 0

        if key != None:
            self.insert(key)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'NaryTree({} nodes)'.format(self.size)

    def insert(self, key):

        for letter in key:
            node = NaryTreeNode(letter)
            if node not in node.children:
                node = NaryTreeNode(letter)
                node.children.append(node)
                print(node)
                self.size += 1
        return node.children

naryTree = NaryTree('redi')
print('tree', naryTree)
