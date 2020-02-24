#!python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        # print("self in leaf : ", self.left)
        return self.left == None and  self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: 0(n) under what conditions the
        function height have to be called n times before it returns a value.
        o(1) if the node is a leaf node"""
        # TODO: Check if left child has a value and if so calculate its height

        if self.right and self.left:
            return 1 + max(self.right.height(), self.left.height())
        elif self.right:
            return 1 + self.right.height()
        else:
            return 0




class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: O(h) under what conditions? it has
        to iterate h times before it returns the height"""
        # TODO: Check if root node has a value and if so calculate its height
        if self.root:
            return self.root.height()
        return 0

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: log(n) under what conditions? If tree is balanced
        TODO: Worst case running time: O(n) under what conditions? If tree is structured as a list in one direction"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: log(n) under what conditions? If tree is balanced
        TODO: Worst case running time: O(n) under what conditions? If tree is structured as a list in one direction"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: log(n) under what conditions? if
        we can manage to have a balanced tree we can insert item by
        ignoring the other half of the tree after comparing
        TODO: Worst case running time: 0(n) under what conditions? if items
        passed were soreted in reverse manner we will end up having a liner tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # TODO: Check if the given item should be inserted left of parent node
        if parent < item:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # TODO: Check if the given item should be inserted right of parent node
        elif parent > item:
            # TODO: Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # TODO: Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: log(n) under what conditions? If tree is balanced
        TODO: Worst case running time: O(n) under what conditions? If tree is unbalanced(Structured in one direction)"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: O(log n) under what conditions?
        If we have a balanced tree
        TODO: Worst case running time: O(n) under what conditions?
        If we have a tree that is structured in one direction """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: log(n) under what conditions?
        if our tree is a balanced tree.
        TODO: Worst case running time: O(n) under what conditions?
        if our tree is a one way tree like a list"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion). Time-Complexity --> log(n)"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            # parent = node.data
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            if node.left != None:
                parent = node
                node = node.left
                return self._find_parent_node_recursive(item, node, parent) # Hint: Remember to update the parent parameter
            node.left = BinaryTreeNode(item)
            return node.left.data
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            if node.right != None:
                parent = node
                node = node.right
                return self._find_parent_node_recursive(item, node, parent)  # Hint: Remember to update the parent parameter
            node.right = BinaryTreeNode(item)
            return node.right.data

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        if self.search(item):
            return self._delete(item)
        else:
            raise ValueError('Item Not Found')
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def _delete(self, item):
        parent = self._find_parent_node_iterative(item)
        node = self._find_node_iterative(item)
        # node is only child
        if node.left == None and node.right == None:
            if node.data < parent.data:
                parent.left = None
            else:
                parent.right = None
        # node has a left child only
        elif node.left and node.right == None:
            if node.data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
        # node has a right child only
        elif node.left == None and node.right:
            if node.data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
        # node has a left and right child
        else:
            delnode = node
            delnodeparent = parent
            while delnode.left:
                delnodeparent = delnode
                delnode = delnode.left
            if delnode.right:
                if delnode.right.data > delnodeparent.data:
                    delnodeparent.right = delnode.right
                else:
                    delnodeparent.left = delnode.right
            else:
                if delnode.data > delnodeparent.data:
                    delnodeparent.right = None
                else:
                    delnodeparent.left = None



    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions? we have to
        traverse all the nodes to add them to item list
        TODO: Memory usage: O(h) Why and under what conditions? where h is
        the height of the tree and space required is proportional to the height
        of the tree which can be equal to the number of nodes in the tree in the worst case"""
        if node:

            # TODO: Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Traverse right subtree, if it exists

            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions? we have to
        traverse all the nodes to add them to item list
        TODO: Memory usage: O(h) Why and under what conditions? where h is
        the height of the tree and space required is proportional to the height
        of the tree which can be equal to the number of nodes in the tree in the worst case"""

        if node:
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            # TODO: Traverse right subtree, if it exists

            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions? we have to
        traverse all the nodes to add them to item list
        TODO: Memory usage: O(h) Why and under what conditions? where h is
        the height of the tree and space required is proportional to the height
        of the tree which can be equal to the number of nodes in the tree in the worst case"""
        if node:
            # TODO: Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # TODO: Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # TODO: Visit this node's data with given function
            visit(node.data)



    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        # queue = ...
        # TODO: Enqueue given starting node
        # ...
        # TODO: Loop until queue is empty
        # while ...:
            # TODO: Dequeue node at front of queue
            # node = ...
            # TODO: Visit this node's data with given function
            # ...
            # TODO: Enqueue this node's left child, if it exists
            # ...
            # TODO: Enqueue this node's right child, if it exists
            # ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()


    # print("leaf: ", node.is_leaf())
    # print("is_branch: ", node.is_branch())


    # print('tree: {}'.format(tree))
    # print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))




    # print('tree: {}'.format(tree))
    # print('root: {}'.format(tree.root))
    # print('root right: {}'.format(tree.root.right))
    # print('root left: {}'.format(tree.root.left))
    # print('root right right: {}'.format(tree.root.right.right))
    # print('root right left: {}'.format(tree.root.right.left))
    # print('root left left: {}'.format(tree.root.left.left))
    # print('root left right: {}'.format(tree.root.left.right))
    # print('root right right right: {}'.format(tree.root.right.right.right))
    # print('root right right left: {}'.format(tree.root.right.right.left))
    # print('root left left left: {}'.format(tree.root.left.left.left))
    # print('root left left right: {}'.format(tree.root.left.left.right))

    print("height in tree", tree.height())

    # print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 3
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))
    # # del_item = tree.delete(7)
    # print("7 Removeed", tree.search(7))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
